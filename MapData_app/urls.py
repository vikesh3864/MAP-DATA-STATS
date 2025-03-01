from django.urls import path
from .views import home,get_locations, get_statistics

urlpatterns = [
    path('',home, name='home'),
    path('locations/',get_locations, name='locations'),
    path('statistics/', get_statistics, name='statistics'),
]