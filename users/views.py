from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from django.shortcuts import render
from users.models import CustomUser
from django.http import HttpResponseRedirect



class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def ChangeProfile(request, user_id):
    """Редактирует существующий профиль"""
    if request.user.id == user_id:
        user = CustomUser.objects.get(id=user_id)
        image = user.image
        if request.method != 'POST':
            # Исходный запрос; форма заполняется данными текущей записи
            form = CustomUserChangeForm(instance=user)
        else:
            # отправка данных POST; обработать данные
            form = CustomUserChangeForm(instance=user, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('recipes:home'))
        context = {'form': form, 'image': image}
        return render(request, 'users/change_form.html', context)
    else:
        raise Http404





