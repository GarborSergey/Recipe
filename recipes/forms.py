from django import forms
from .models import Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['category', 'name', 'introduction', 'ingredients_input', 'time_cook', 'recipe']
        labels = {'category': 'Категория блюда', 'name': 'Название', 'introduction': 'Краткое описание',
                  'ingredients_input': 'Ингредиенты. Вводите каждый ингредиент с новой строки!', 'time_cook': 'время приготовления', 'recipe': 'рецепт'}

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False) # делает поле необязательным
    message = forms.CharField(widget=forms.Textarea)
