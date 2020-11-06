from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile



class UserRegiseterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["Ecole", "niveau", "profession", "DomainDePredilection", "Bio", "image"]
