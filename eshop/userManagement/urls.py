from django.urls import path
from .views import *

urlpatterns = [
    path('login/',user_login, name='login'),
    path('signup/',user_signUp, name='signup'),
    path('login/confirmLogin',confirmLogin, name='confirmLogin')

]
