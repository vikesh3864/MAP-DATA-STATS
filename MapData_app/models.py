from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=260)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name