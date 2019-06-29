from django.contrib import admin
from django.urls import path, include
from accounts import views
app_name="accounts"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluationReject/', views.evaluationReject, name='evaluationReject'),
    path('loading/', views.loading, name='loading'),
    path('menu/', views.menu, name='menu'),
    path('loading2/', views.loading2, name='loading2'),
    path('success/<int:r_type>', views.success, name='success'),
    path('requestForm/', views.requestForm, name='requestForm'),
    path('agree/', views.agree, name='agree'),
    path('finish/<str:tx>/<str:cut_rate>', views.finish, name='finish'),
    path('KBscan/', views.KBscan, name='KBscan'),
]
