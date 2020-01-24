from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('manageProduct/',view_manage_page,name='product'),
    
    path('manageProduct/addPhoneForm',ForPhones.view_phone_form, name='phone'),
    path('manageProduct/addPhoneForm/save',ForPhones.save_phone_database),
    path('manageProduct/phoneUpdate/edit/',ForPhones.get_phone_id),
    path('manageProduct/phoneUpdate/edit/update/<int:id>',ForPhones.update_phones),

    path('manageProduct/accessoriesForm',ForAccessories.view_accessories_form, name='accessories'),
    path('manageProduct/accessoriesForm/save',ForAccessories.save_accessories),    
    path('manageProduct/accessoriesUpdate/edit/',ForAccessories.get_acc_id),
    path('manageProduct/accessoriesUpdate/edit/update/<int:id>',ForAccessories.update_accessories),

    path('manageProduct/delete',deleteProducts,name='deleteProducts'),
    path('manageProduct/confirmdelete/<int:ID>',confirmDeleteProducts),
]
