# users/urls.py

from django.urls import path
from .views import register,profile,add_food_item,food_list,home,search,custom_login,custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', custom_logout, name='custom_logout'),
    path('add-food-item/', add_food_item, name='add_food_item'),  # New food item URL
    path('food-list/', food_list, name='food_list'),
    path('search/', search, name='search'),
]
