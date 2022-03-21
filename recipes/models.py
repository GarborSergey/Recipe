from django.db import models

# Create your models here.

class DishCategory(models.Model):
    """Категория блюда (первое, второе итд)"""
    dish_category = models.CharField(max_length=150, verbose_name='категория блюда')

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.dish_category


class Ingredients(models.Model):
    """Ингредиенты"""
    name = models.CharField(max_length=50, verbose_name='ингредиент')

    def __str__(self):
        return self.name

class Dish(models.Model):
    """Блюдо"""
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, verbose_name='категория блюда')
    name = models.CharField("наименование блюда", max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField('краткое описание блюда')
    ingredients_input = models.ManyToManyField(Ingredients, verbose_name='ингредиенты')
    ingredients_num = models.CharField("количество ингредиентов", max_length=3)
    time_cook = models.CharField("время приготовления", max_length=30)
    recipe = models.TextField("рецепт блюда")

    def __str__(self):
        return self.name
