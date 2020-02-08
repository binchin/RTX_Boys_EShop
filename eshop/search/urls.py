from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('search/',view_search, name='search'),
]
