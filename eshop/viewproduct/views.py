from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from productmanagement.models import Product,Phones,Accessories,Laptop
# Create your views here.

# homepage
def homepage(request):
    product = Product.objects.all()
    params = {'products':product}
    return render(request,'viewproduct/home.html',params)

# displaying specific product
def viewProductDetails(request,ID):
    product = Product.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'viewproduct/view.html',context_varible)


def viewPhones(request):
    return render(request,'viewproduct/phones.html',params)

def viewLaptops(request):
    return render(request,'viewproduct/laptops.html',params)

def viewAccessories(request):
    return render(request,'viewproduct/accessories.html',params)
