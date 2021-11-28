from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
Register Form to Register a New User 
With Email Field
"""


class RegisterUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadImage(forms.ModelForm):
    iamge=forms.ImageField()

    # class Meta:

