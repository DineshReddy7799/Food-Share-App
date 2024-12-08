from django.contrib import admin
from .models import CustomUser,FoodItem
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(FoodItem)
