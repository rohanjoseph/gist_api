from django.contrib import admin
from django.urls import path
from dataWare import views

urlpatterns = [
    path('data',views.data, name='data'),
    path('index',views.index, name='index')
]
