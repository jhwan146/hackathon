from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluationReject/', views.evaluationReject, name='evaluationReject'),
    path('loading/', views.loading, name='loading'),
    path('menu/', views.menu, name='menu')
]
