from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('calculator/', views.calculator, name='calculator'),
    path('currency/', views.currency, name='currency'),
    path('all_members/', views.all_members, name='all_members'),

]