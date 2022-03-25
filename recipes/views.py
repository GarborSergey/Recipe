from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .forms import DishForm, ContactForm
from recipes.models import DishCategory, Dish
from django.urls import reverse
from django.core.mail import send_mail
from recipe import settings
from django.contrib.auth.decorators import login_required
import random

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


def dish(request, dish_id):
    """Выводит рецепт блюда"""
    dish = Dish.objects.get(id=dish_id)
    context = {'dish': dish}
    return render(request, 'recipes/dish.html', context)


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

@login_required
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


def contact(request):
    """Обратная связь"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'] + ' отправленно пользователем:' + cd['email'],
                settings.EMAIL_HOST_USER,
                ['garborfersru@gmail.com']
            )
            return render(request, 'recipes/thanks_form.html')
    else:
        form = ContactForm(
            initial={'subject': 'Мне очень нравится ваш сайт!'}
        )
    return render(request, 'recipes/contact_form.html', {'form': form})

def random_dish(request):
    all_dish = Dish.objects.all()
    dish = random.choice(all_dish)
    context = {'dish': dish}
    return render(request, 'recipes/dish.html', context)