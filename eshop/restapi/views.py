from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from productmanagement.models import Product,Phones,Laptop,Accessories
import json
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def getProductDetails(request,ID):
    if request.method == "GET":
        # to search product in their tables
        try:
            products = Product.objects.get(id = ID)
        except Product.DoesNotExist:
            return JsonResponse({
                "product":"none"
            })
        
        
        # finding in which table exists
        try:
            phone = Phones.objects.get(product_id=ID)
            product = 'phone'
        except Phones.DoesNotExist:
            accessories = Accessories.objects.get(product_id=ID)
            product = 'accessories'
        except Accessories.DoesNotExist:
            laptop = Laptop.objects.get(product_id=ID)
            product = 'laptop'


        # converting file fields into string
        img = str(products.image.url)
        spec = str(products.specs.url)
        
        # below code checks whether the product is phone,laptop or accessories and sends json response acordingly
        if (product == 'phone'):
            return JsonResponse({
                "product":"phone",
                "id":products.id,
                "name":products.name,
                "price":products.price,
                "image":img,
                "specs":spec,
                "brand":products.brand,
                "screenSize":phone.screenSize,
                "color":phone.color,
                "RAM":phone.RAM,
                "ROM":phone.ROM,
                "battery":phone.battery,
                "description":phone.description
            })

        elif(product == 'laptop'):
            return JsonResponse({
                "product":"laptop",
                "id":products.id,
                "name":products.name,
                "price":products.price,
                "image":img,
                "specs":spec,
                "brand":products.brand,
                "screenSize":laptop.screenSize,
                "color":laptop.color,
                "RAM":laptop.RAM,
                "HDD":laptop.ROM,
                "battery":laptop.battery,
                "description":laptop.description,
                "cpu":laptop.cpu,
                "graphics":laptop.graphics,
                "weight":laptop.weight,
            })
        elif(product == 'accessories'):
            return JsonResponse({
                "product":"accessories",
                "id":products.id,
                "name":products.name,
                "image":img,
                "specs":spec,
                "brand":products.brand,
                "category":accessories.category,
                "description":accessories.description
            })
    
    else:
        return JsonResponse({
        "product":"none"
        })



