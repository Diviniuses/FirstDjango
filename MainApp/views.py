from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = """
    <h1>Изучаем Django</h1>
    <strong>Автор</strong>
    """
    return HttpResponse(text)

def about_page(request):
    text = """
    <h1>Имя: Иван</h1>
    <p>Отчество: Петрович</p>
    <p>Фамилия: Иванов</p>
    <p>Телефон: 8-923-600-01-02</p>
    <p>Email: vasya@mail.ru</p>
    """
    return HttpResponse(text)

items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Соса-сola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},
]

def item_detail(request, item_id):
    for item in items:
        if item['id'] == item_id:
            return HttpResponse(f"<h1>{item['name']}</h1>")
    
    # Товар не найден 
    return HttpResponse(f"<h1>Товар с id={item_id} не найден</h1>", status=404)

'''Cписок товаров'''
def items_list(request):
    items_html = "<ol>"
    for item in items:
        items_html += f'<li><a href="/item/{item["id"]}">{item["name"]}</a></li>'
    items_html += "</ol>"
    
    return HttpResponse(items_html)