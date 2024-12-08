# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from geopy.geocoders import Nominatim

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, help_text="Enter the place name or address.")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.location:
            self.latitude, self.longitude = geocode_location(self.location)
        super().save(*args, **kwargs)

def geocode_location(location_name):
    geolocator = Nominatim(user_agent="food_share_app")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    return None, None
