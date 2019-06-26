from django.contrib import admin
from django.urls import path, include
from bank import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('index/', views.index),
    path('passed/', views.passed, name='passed'),
    path('rejected/', views.rejected, name='rejected'),
    path('total/', views.total, name='total'),
    path('login/', views.login, name='login'),
]
