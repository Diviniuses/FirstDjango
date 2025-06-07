from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseNotFound

def home(request):
    context = {
        'title': 'Главная страница',
        'header': 'Добро пожаловать в наш магазин',
        'description': 'Здесь вы можете найти все, что вам нужно'
    }
    return render(request, 'MainApp/index.django.html', context)

def about_page(request):
    context = {
        'title': 'О нас',
        'header': 'Информация о нас',
        'name': 'Иван',
        'middle_name': 'Петрович',
        'surname': 'Иванов',
        'phone': '8-923-600-01-02',
        'email': 'vasya@mail.ru'
    }
    return render(request, 'MainApp/about.html', context)

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 3},
    {"id": 3, "name": "Соса-сola 1 литр", "quantity": 10},
    {"id": 4, "name": "Картофель фри", "quantity": 7},
    {"id": 5, "name": "Кепка", "quantity": 0}
]

def item_detail(request, item_id):
    return redirect('items_list')

'''Cписок товаров'''
def items_list(request):
    context = {
        'title': 'Список товаров',
        'header': 'Наши товары',
        'items': items
    }
    return render(request, 'MainApp/items_list.html', context)