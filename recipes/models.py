from django.db import models


# Create your models here.

class DishCategory(models.Model):
    """Категория блюда (первое, второе итд)"""
    dish_category = models.CharField(max_length=150, verbose_name='категория блюда')
    image = models.ImageField(upload_to='image/recipes', null=True, blank=True, verbose_name='Картики категорий')
    intro = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.dish_category



class Dish(models.Model):
    """Блюдо"""
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, verbose_name='категория блюда')
    name = models.CharField("наименование блюда", max_length=200)
    image = models.ImageField(upload_to='images/recipes', null=True, blank=True, verbose_name='фото готового блюда')
    date_added = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField('краткое описание блюда')
    ingredients_input = models.TextField(verbose_name='ингредиенты')
    ingredients_num = models.IntegerField()
    time_cook = models.CharField("время приготовления", max_length=30)
    recipe = models.TextField("рецепт блюда")
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

