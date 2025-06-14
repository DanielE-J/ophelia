# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from menu import views

def food(request):
    """
    a view to display the food menu
    """
    food_list = FoodItem.objects.all()
    return render(
        request, 'menu/food.html', {'food_list': food_list})


def drinks(request):
    """
    a view to display the drinks menu
    """
    drink_list = DrinkItem.objects.all()
    return render(
        request, 'menu/drinks.html', {'drink_list': drink_list})
    
def menu(request):
    # Your logic here
    return render(request, 'menu/menus.html')