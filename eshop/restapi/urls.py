from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('getProductDetails/<int:ID>',getProductDetails),
    path('getAllProducts/',getAllProducts),
]
