from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from productmanagement.models import Product,Phones,Laptop,Accessories
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group

# Get a specific model data by ID => GET
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
        
        
        # finding in which table does the product exists
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
                "price":products.price,
                "image":img,
                "specs":spec,
                "brand":products.brand,
                "category":accessories.category,
                "description":accessories.description
            })
    
    else:
        return JsonResponse({
            "message":"Only get request available"
        })

# GET data url: http://127.0.0.1:8000/api/getProductDetails/<product-id>

# Get all model data => GET
@csrf_exempt
def getAllProducts(request):
    if request.method == "GET":
        products = Product.objects.all()
        list_of_products = list(products.values("name","price"))
        productDictionary = {
            "products":list_of_products
        }
        return JsonResponse(productDictionary)
    else:
        return JsonResponse({
            "message":"Only get request available"
        })


# Post model data => POST
@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        dictionary_object = json.loads(request.body)
        user = User.objects.create_user(username=dictionary_object['Username'],password=dictionary_object['Password'],email=dictionary_object['Email'],first_name=dictionary_object['Fname'],last_name=dictionary_object['Lname'])
        user.save()
        group = Group.objects.get(name='Customers') 
        group.user_set.add(user)
        
        return JsonResponse({
            "message":"Successfully created user"
        })

    else:
        return JsonResponse({
            "message":"Only POST request available"
        })
# post data url: http://127.0.0.1:8000/api/createUser/
# post data format: {"Username":"testuser","Password":"test@password","Email":"testuser@eshop.com","Fname":"Eshop","Lname":"Bahadur"}


# Update a specific model data by ID => PUT
@csrf_exempt
def updateProductPrice(request):
    if request.method == 'PUT':
        dictionary_object = json.loads(request.body)
        product = Product.objects.get(id=dictionary_object['id'])
        product.price = id=dictionary_object['price']
        product.save()
        return JsonResponse({
            "message":"Successfully updated price"
        })
    
    else:
        return JsonResponse({
            "message":"Only PUT request available"
        })

# PUT data url: http://127.0.0.1:8000/api/updateProductPrice/
# PUT data format: {"id":"1","price":"105000"}

# Delete a specific model data by ID => DELETE
@csrf_exempt
def deleteProduct(request,ID):
    if request.method == 'DELETE':
        Product.objects.get(id=ID).delete()
        return JsonResponse({
            "message":"Successfully deleted product"
        })
    
    else:
        return JsonResponse({
            "message":"Only Delete request available"
        })

# DELETE data url: http://127.0.0.1:8000/api/deleteProduct/<product-id>

#Rest API Pagination
# Pagination with SIZE and PAGENO params => GET

# http://127.0.0.1:8000/api/pagination/<int:SIZE>/<int:PAGENO>
def getPage(request, SIZE, PAGENO):
    if request.method == 'GET':
        # determining start 
        start = ((PAGENO -1)* SIZE)

        # determining end
        end = start + SIZE
        print(start," End:",end)
        products = Product.objects.all()[start:end]
        list_of_products = list(products.values("name","price","stockNo","brand"))
        productDictionary = {
            "products":list_of_products
        }
        return JsonResponse(productDictionary)

    else:
        return JsonResponse({
            "message":"Only get request available"
        })


