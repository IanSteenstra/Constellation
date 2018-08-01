from django.urls import path
from . import views
from home import views as home_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('new_exp/', views.new_exp, name='new_exp'),
    path('home/', home_views.index, name='index'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]  
