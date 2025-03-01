from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Location
from MapData_app.serializers import LocationSerializer
from django.db.models import Count
import json

def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def get_locations(request):
    locations = Location.objects.all()
    data={
        "type": "FeatureCollection",
        "features":[
            {
                "type":"Feature",
                "geometry":{
                    "type":"Point",
                    "coordinates":[loc.longitude,loc.latitude]
                },
                "properties": {
                    "name": loc.name,
                    "category":loc.category,
                }
            }for loc in locations
        ]
    }
    return Response(data)

@api_view(['GET'])
def get_statistics(request):
    total_locations = Location.objects.count()
    most_common_category = Location.objects.values('category').annotate(count=Count('category')).order_by('-count').first()

    stats = {
        "total_locations": total_locations,
        "most_common_category":most_common_category['category'] if most_common_category else None
    }
    return Response(stats)


# Create your views here.
