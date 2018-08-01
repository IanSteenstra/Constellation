from django.urls import path
from . import views
from users import views as usr_views
from django.contrib.auth import views as auth_views
#import django_cas_ng.views as cas_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/home/'}, name='logout'),
    path('new_prod/', views.new_prod, name='new_prod'),
    path('profile/', usr_views.profile, name='profile'),
    path('new_user/', usr_views.new_user, name='new_user')
    # path('accounts/login/', cas_views.login, name='cas_ng_login'),
    # path('accounts/logout/', cas_views.logout, name='cas_ng_logout'),
]
