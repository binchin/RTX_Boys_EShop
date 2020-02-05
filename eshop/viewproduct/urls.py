from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('view/<int:ID>',viewProductDetails)
    path('phones/', viewPhones,name='phones'),
    path('laptops/', viewLaptops,name='laptops'),
    path('accessories/',viewAccessories,name='accessories'),
]
