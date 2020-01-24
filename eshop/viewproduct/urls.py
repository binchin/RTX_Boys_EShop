from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('view/<int:ID>',viewProductDetails)
    # path('viewPhones/', seePhones),
    # path('viewLaptops/', seeLaptops),
    # path('viewAccessories/',seeAccessories),
]
