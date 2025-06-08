from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item

def home(request):
    context = {
        'title': 'Главная страница',
        'header': 'Добро пожаловать в наш магазин',
        'description': 'Здесь вы можете найти все, что вам нужно'
    }
    return render(request, 'MainApp/index.html', context)

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

def item_detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        context = {
            'item': item,
            'header': item.name
        }
        return render(request, 'MainApp/item.html', context)
    except Item.DoesNotExist:
        return HttpResponseNotFound(f"Товар с id {item_id} не найден")

'''Cписок товаров'''
def items_list(request):
    items = Item.objects.all().order_by('id')
    print("Items from database:", [f"{item.id}: {item.name} - {item.quantity}" for item in items])
    context = {
        'title': 'Список товаров',
        'header': 'Наши товары',
        'items': items
    }
    return render(request, 'MainApp/items_list.html', context)