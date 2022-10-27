from dataclasses import Field
from django import forms
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form

from models import UserProfile  
class UserProfileCreationForm(UserCreationForm):
    class meta:
        model = UserProfile
        fields = {'username','password'}
