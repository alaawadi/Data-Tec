import email
from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile
from django.conf import settings

class SignupForm(UserCreationForm):
    # username = forms.CharField(unique=True)
    # email = forms.EmailField(unique=True)
    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2']
        

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields= ['username','first_name','last_name','email'] 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone_number','image']