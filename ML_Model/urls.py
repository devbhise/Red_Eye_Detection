
from unicodedata import name
from django.contrib import admin
from django.urls import path
from ML_Model import views
urlpatterns = [
    path("", views.index, name='index'),
    path("result",views.result,name='result'),
]