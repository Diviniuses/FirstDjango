from django.contrib import admin
from .models import Item, Color

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'quantity', 'description')
    list_filter = ('brand',)
    search_fields = ('name', 'brand', 'description')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
