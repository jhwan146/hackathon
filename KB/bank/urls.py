from django.contrib import admin
from django.urls import path, include
from bank import views

urlpatterns = [
    path('main/', views.main),
    path('index/', views.index),
    path('passed/', views.passed),
    path('rejected/', views.rejected),
    path('total/', views.total),
]
