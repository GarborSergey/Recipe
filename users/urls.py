from django.urls import path, re_path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('change_profile/<int:user_id>', views.ChangeProfile, name='change_profile')
]