# Generated by Django 4.0.3 on 2022-03-30 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_dish_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
