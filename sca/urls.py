from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('calculator/', views.calculator, name='calculator'),
    path('currency/', views.currencypage, name='currency'),
    path('currency/details/<int:id>', views.details, name='details'),
    
    path('all_members/', views.all_members, name='all_members'),
    path('all_members/details/<int:id>', views.details, name='details'),
 

 

]