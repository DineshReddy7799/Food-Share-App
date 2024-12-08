from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, FoodItemForm
from .models import FoodItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import FoodItem
from django.core.serializers import serialize
import json
from django.shortcuts import render
from .models import FoodItem
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import auth


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect the user after login (set the URL as per your need)
                return redirect('profile')  # or 'profile' or wherever you'd like to redirect
            else:
                # If authentication failed, return error
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def custom_logout(request):
    auth.logout(request)

    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login or another page
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/profile.html', {'form': form})


@login_required
def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')  # Adjust the redirect as needed
    else:
        form = FoodItemForm()
    return render(request, 'users/add_food_item.html', {'form': form})





@login_required
def food_list(request):
    # Serialize food items for JavaScript
    food_items = FoodItem.objects.all()
    food_items_json = json.dumps([
        {
            "name": item.name,
            "location": item.location,
            "latitude": float(item.latitude) if item.latitude else None,
            "longitude": float(item.longitude) if item.longitude else None
        }
        for item in food_items
    ])
    return render(request, 'users/food_list.html', {'food_items_json': food_items_json})

from django.shortcuts import render
from .models import FoodItem

def home(request):
    # Get a few featured food items from the database
    featured_food_items = FoodItem.objects.all()[:5]  # Adjust the slice as needed
    context = {
        'featured_food_items': featured_food_items,
    }
    return render(request, 'users/home.html', context)


# users/views.py

from django.shortcuts import render
from .models import FoodItem

def search(request):
    query = request.GET.get('q')
    food_items = FoodItem.objects.filter(name__icontains=query) if query else FoodItem.objects.none()
    context = {
        'food_items': food_items,
        'query': query,
    }
    return render(request, 'users/search_results.html', context)

