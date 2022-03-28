from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='images/users', null=True, blank=True, verbose_name='аватар')