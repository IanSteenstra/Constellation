from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_prod/', views.new_prod, name='new_prod'),
]