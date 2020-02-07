from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('getProductDetails/<int:ID>',getProductDetails),
    path('getAllProducts/',getAllProducts),
    path('createUser/',createUser),
    path('updateProductPrice/',updateProductPrice),
    path('deleteProduct/<int:ID>',deleteProduct),
]
