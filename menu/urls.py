from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('food/', views.food, name='food'),
    path('drinks/', views.drinks, name='drinks'),
]