from django.contrib.auth.models import AbstractUser
from django.db import models
from recipes.models import Dish

class CustomUser(AbstractUser):
    """Пользователи"""
    fullname = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='images/users', null=True, blank=True, verbose_name='аватар')
    liked_dish = models.ManyToManyField(Dish)


class Comment(models.Model):
    """Комментарий"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    text = models.TextField('Комментарий', max_length=73)
    date_added = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.text
