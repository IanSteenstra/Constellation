from django.urls import path
from . import views
#import django_cas_ng.views as cas_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/home/'}, name='logout'),
    path('new_prod/', views.new_prod, name='new_prod'),
    # path('accounts/login/', cas_views.login, name='cas_ng_login'),
    # path('accounts/logout/', cas_views.logout, name='cas_ng_logout'),
]
