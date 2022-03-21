from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .forms import DishForm
from recipes.models import DishCategory, Dish
from django.urls import reverse

def home(request):
    return render(request, 'recipes/home.html')

def dish_categories(request):
    """Выводит все категории блюд"""
    dish_categories = DishCategory.objects.all()
    context = {'dish_categories': dish_categories}
    return render(request, 'recipes/dish_categories.html', context)

def category(request, category_id):
    """Выводит все блюда из категории"""
    category = DishCategory.objects.get(id=category_id)
    dishes = category.dish_set.all()
    context = {'category': category, 'dishes': dishes}
    return render(request, 'recipes/dishes.html', context)

def search(request):
    """Поиск по названию блюда"""
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
        elif len(q) > 20:
            errors.append('Поисковый запрос должен содержать не больше 20 символов!')
        else:
            dishes = Dish.objects.filter(name__icontains=q)
            context = {'dishes': dishes, 'query': q}
            return render(request, 'recipes/result_form.html', context)
    return render(request, 'recipes/search_form.html', {'errors': errors})

def new_dish(request):
    """Добавление нового рецепта"""
    if request.method != 'POST':
        form = DishForm()
    else:
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recipes:home'))
    context = {'form': form}
    return render(request, 'recipes/new_dish.html', context)
