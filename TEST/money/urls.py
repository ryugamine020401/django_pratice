from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='Indexmoney'),
    path('update/<str:pk>', views.update, name='Update'),
    path('delete/<str:pk>', views.delete, name='Delete'),
]
