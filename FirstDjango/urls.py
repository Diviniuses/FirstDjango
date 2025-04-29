from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about_page),
    path('item/<int:item_id>/', views.item_detail),
    path('items/', views.items_list),
]
