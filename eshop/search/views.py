from django.shortcuts import render
from django.template import Template,context
from productmanagement.models import Product,Phones,Accessories,Laptop
# Create your views here.


#  ***SEARCH FUNCTIONALITY***
def view_search(request):
    query=request.GET['query']  
    products= Product.objects.filter(name__icontains=query)
    context_variable={'products': products, 'query': query}
    return render(request,'search.html',context_variable)


def view_product(request,ID):
    product = Phones.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'view2.html',context_varible)

