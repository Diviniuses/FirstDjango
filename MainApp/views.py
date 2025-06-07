from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

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
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 3},
    {"id": 3, "name": "Соса-сola 1 литр", "quantity": 10},
    {"id": 4, "name": "Картофель фри", "quantity": 7},
    {"id": 5, "name": "Кепка", "quantity": 0}
]

def item_detail(request, item_id):
    try:
        item_id = int(item_id)
        for item in items:
            if item['id'] == item_id:
                return HttpResponse(f"""
                    <h1>{item['name']}</h1>
                    <p>Количество товара: {item['quantity']}</p>
                    <p><a href="/items/">Назад к списку товаров</a></p>
                """)
        
        # Товар не найден 
        return HttpResponseNotFound(f'Товар с id={item_id} не найден')
    except ValueError:
        return HttpResponseNotFound('Неверный формат ID товара')

'''Cписок товаров'''
def items_list(request):
    items_html = "<ol>"
    for item in items:
        items_html += f'<li><a href="/item/{item["id"]}">{item["name"]}</a> (Количество: {item["quantity"]})</li>'
    items_html += "</ol>"
    
    return HttpResponse(items_html)