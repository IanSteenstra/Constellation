from django.urls import path
from . import views
from home import views as home_views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('new_exp/', views.new_exp, name='new_exp'),
    path('home/', home_views.index, name='index')
]  
