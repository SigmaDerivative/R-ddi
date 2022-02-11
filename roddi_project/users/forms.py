# Her skal vi lage en selvlagd form for brukere

from django.contrib.auth.models import User  # importere bruker tabellen
# importere default form for registrering
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# form for å oppdatere bilde.


class ImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cellphone_number', 'address', 'image']
