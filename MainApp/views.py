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