from django.db import models
from users.models import CustomUser

# Create your models here.

class DishCategory(models.Model):
    """Категория блюда (первое, второе итд)"""
    dish_category = models.CharField(max_length=150, verbose_name='категория блюда')

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.dish_category



class Dish(models.Model):
    """Блюдо"""
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, verbose_name='категория блюда')
    name = models.CharField("наименование блюда", max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField('краткое описание блюда')
    ingredients_input = models.TextField(verbose_name='ингредиенты')
    ingredients_num = models.IntegerField()
    time_cook = models.CharField("время приготовления", max_length=30)
    recipe = models.TextField("рецепт блюда")

    def __str__(self):
        return self.name

class Comment(models.Model):
    """Комментарий"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    text = models.TextField('Комментарий', max_length=73)
    date_added = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text
