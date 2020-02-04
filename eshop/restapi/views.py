from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from productmanagement.models import Product,Phones,Laptop,Accessories
import json
from django.core.exceptions import ObjectDoesNotExist
# try:
#     go  = Content.objects.get(name="baby")
# except ObjectDoesNotExist:
#     go = None

@csrf_exempt
def getProductDetails(request,ID):
    if request.method == "GET":
        # to search product in their tables
        product = Product.objects.get(id = ID)
        # finding in which table exists
        phone = Phones.objects.get(product = ID)
        laptop = Laptop.objects.filter(product = ID)
        accessories = Accessories.objects.get(product = ID)
        # print(str(product.image.url))
        img = str(product.image.url)
        spec = str(product.specs.url)
        # below code checks whether the product is phone,laptop or accessories and sends json response acordingly
        if (phone is not None):
            return JsonResponse({
                "product":"phone",
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "image":img,
                "specs":spec,
                "brand":product.image,
                "screenSize":phone.screenSize,
                "color":phone.color,
                "RAM":phone.RAM,
                "ROM":phone.ROM,
                "battery":phone.battery,
                "description":phone.description
            })
        elif(laptop is not None):
            return JsonResponse({
                "product":"laptop",
                "id":product.id,
                "name":product.name,
                "price":product.price,
                "image":img,
                "specs":spec,
                "brand":product.image,
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
        elif(accessories is not None):
            return JsonResponse({
                "product":"accessories",
                "id":product.id,
                "name":product.name,
                "image":img,
                "specs":spec,
                "specs":product.specs,
                "brand":product.image,
                "category":accessories.category,
                "description":accessories.description
            })
        else:
            return JsonResponse({
                "product":"null"
            })
    else:
        return JsonResponse({
        "message":"null"
        })

