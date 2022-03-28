from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'fullname', 'image')
        labels = {'username': 'логин', 'email': 'e-mail', 'fullname': 'полное имя', 'image': 'аватар профиля'}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fullname', 'image')
        labels = {'username': 'логин', 'email': 'e-mail', 'fullname': 'полное имя', 'image': 'аватар профиля'}