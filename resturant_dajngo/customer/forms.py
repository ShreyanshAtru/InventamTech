from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class SignUpForm(UserCreationForm):
    
    class Meta:
        model=User
        fields = ('email', 'username', 'is_superuser', 'is_staff')
    