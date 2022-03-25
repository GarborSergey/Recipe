from django.urls import path, re_path
from . import views

app_name = 'recipes'

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Страница с категориями блюд
    path('dish_category', views.dish_categories, name='dish_categories'),
    # Страница со всеми блюдами из категории
    path('dish_category/<int:category_id>', views.category, name='category'),
    # Страница с поиском
    path('search/', views.search, name='search'),
    # Страница с добовлением нового рецепта
    path('new_dish/', views.new_dish, name='new_dish'),
    # Страница с обратной связью
    path('contact/', views.contact, name='contact'),
    # Страница с рецептом
    path('dish/<int:dish_id>', views.dish, name='dish'),
    # Страница со случайным рецептом
    path('random_dish/', views.random_dish, name='random_dish')

]