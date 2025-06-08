from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название цвета')
    
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['name']

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    description = models.TextField(default='', verbose_name='Описание')
    brand = models.CharField(max_length=100, default='', verbose_name='Бренд')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.name} ({self.brand})"

class ItemColor(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Цвет товара'
        verbose_name_plural = 'Цвета товаров'
        unique_together = ['item', 'color']  # Предотвращает дублирование цветов для одного товара
