# Generated by Django 4.0.3 on 2022-03-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_dish_owner_remove_dish_ingredients_input_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='ingredients_num',
            field=models.IntegerField(),
        ),
    ]
