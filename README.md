    Инструкция по развертыванию проекта:
-Создать виртуальное окружение
'''python3 -m venv django_venv'''
-Активировать виртуальное окружение
'''source django_venv/bin/activate'''
-Установить нужные библиотеки в виртуальное окружение
'''pip install -r requirements.txt'''
-Применить миграции
'''python manage.py migrate'''
-Запустить сервер
'''python manage.py runserver'''