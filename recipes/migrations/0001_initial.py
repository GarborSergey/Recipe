# Generated by Django 4.0.3 on 2022-03-27 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_category', models.CharField(max_length=150, verbose_name='категория блюда')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование блюда')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.TextField(verbose_name='краткое описание блюда')),
                ('ingredients_input', models.TextField(verbose_name='ингредиенты')),
                ('ingredients_num', models.IntegerField()),
                ('time_cook', models.CharField(max_length=30, verbose_name='время приготовления')),
                ('recipe', models.TextField(verbose_name='рецепт блюда')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.dishcategory', verbose_name='категория блюда')),
            ],
        ),
    ]
