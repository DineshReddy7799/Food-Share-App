# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address']


# users/forms.py

from django import forms
from .models import CustomUser

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'address']

# users/forms.py (or food/forms.py if you created a new app)

from django import forms
from .models import FoodItem

'''
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['title', 'description', 'quantity', 'expiration_date', 'image']
'''
# users/forms.py

from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'location']  # Include any other fields you want
