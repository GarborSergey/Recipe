from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from .forms import DishForm, ContactForm, CommentForm
from recipes.models import DishCategory, Dish, Comment
from django.urls import reverse
from django.core.mail import send_mail
from recipe import settings
from django.contrib.auth.decorators import login_required
import random


def ingredients_num(ingredients_field):
    lst_ing = ingredients_field.split('\n')
    return len(lst_ing)


def home(request):
    dish_categories = DishCategory.objects.all()
    context = {'dish_categories': dish_categories}
    return render(request, 'recipes/home.html', context)


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
    comments = Comment.objects.filter(dish=dish_id)
    if request.method != 'POST':
        form_comment = CommentForm()
    else:
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.user = request.user
            comment.dish = dish
            comment.save()
            form_comment = CommentForm(
                initial={'text': ' '}
            )
            context = {'dish': dish, 'form_comment': form_comment, 'comments': comments}
            return render(request, 'recipes/dish.html', context)
    context = {'dish': dish, 'form_comment': form_comment, 'comments': comments}
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
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            new_dish = form.save(commit=False)
            cd = form.cleaned_data
            new_dish.owner = request.user
            new_dish.ingredients_num = len(str(cd['ingredients_input']).split('\n'))
            new_dish.save()
            return HttpResponseRedirect(reverse('recipes:home'))
    context = {'form': form}
    return render(request, 'recipes/new_dish.html', context)


def contact(request):
    """Обратная связь"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['email']:
                cd['message'] += '\nОтправленно пользователем:' + cd['email']
            send_mail(
                cd['subject'],
                cd['message'],
                settings.EMAIL_HOST_USER,
                ['garborfersru@gmail.com']
            )
            return render(request, 'recipes/thanks_form.html')
    else:
        if request.user.is_authenticated and request.user.email:
            form = ContactForm(
                initial={'email': request.user.email}
            )
        else:
            form = ContactForm()
    return render(request, 'recipes/contact_form.html', {'form': form})


def random_dish(request):
    """Случайный рецепт"""
    all_dish = Dish.objects.all()
    dish = random.choice(all_dish)
    url = f"recipes:dish"
    return redirect(url, dish.id)


def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
