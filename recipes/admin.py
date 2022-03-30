from django.contrib import admin
from recipes.models import DishCategory, Dish

class AdminDish(admin.ModelAdmin):
    list_filter = ('date_added',)


admin.site.register(DishCategory)
admin.site.register(Dish, AdminDish)

