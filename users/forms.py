from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Comment


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'fullname', 'image', 'password1')
        labels = {'username': 'логин', 'email': 'e-mail', 'fullname': 'полное имя', 'image': 'аватар профиля'}
        help_texts = {
            'username': '',
        }


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        exclude = ()
        fields = ('username', 'email', 'fullname', 'image', )
        labels = {'username': 'Логин', 'email': 'e-mail', 'fullname': 'Имя', 'image': 'Аватар профиля'}
        help_texts = {
            'username': '',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Прокомментируйте этот рецепт!'}