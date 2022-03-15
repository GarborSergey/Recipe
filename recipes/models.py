from django.db import models

# Create your models here.

class DishCategory(models.Model):
    """Категория блюда (первое, второе итд)"""
    dish_category = models.CharField(max_length=150)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.dish_category

class Dish(models.Model):
    """Блюдо"""
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField()
    ingredients_input = models.TextField()
    ingredients_num = models.CharField(max_length=3)
    time_cook = models.CharField(max_length=20)
    recipe = models.TextField()

