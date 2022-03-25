from django.contrib import admin
from recipes.models import DishCategory, Dish, Ingredients

class AdminDish(admin.ModelAdmin):
    list_filter = ('date_added',)


admin.site.register(DishCategory)
admin.site.register(Dish, AdminDish)
admin.site.register(Ingredients)
