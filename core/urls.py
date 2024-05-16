from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('detail/<pk>/', views.getDetail),
    path('add/', views.addItem),
    path('update/<pk>/', views.updateItem),
    path('delete/<pk>/', views.deleteItem),
]