# Generated by Django 4.0.3 on 2022-03-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_delete_comment'),
        ('users', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='liked_dish',
            field=models.ManyToManyField(blank=True, null=True, to='recipes.dish'),
        ),
    ]
