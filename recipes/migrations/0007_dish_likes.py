# Generated by Django 4.0.3 on 2022-03-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_dishcategory_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
