from django import forms
from .models import Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['category', 'name', 'introduction', 'ingredients_input', 'ingredients_num', 'time_cook', 'recipe']
        labels = {'category': 'Категория блюда', 'name': 'Название', 'introduction': 'Краткое описание',
                  'ingredients_input': 'Ингредиенты', 'ingredients_num': 'кол-во ингредиентов', 'time_cook': 'время приготовления', 'recipe': 'рецепт'}
