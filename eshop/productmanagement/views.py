from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Template,context
from .models import Product
from .models import Phones
from .models import Accessories
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def view_manage_page(request):
    if request.user.is_authenticated:
        return render(request,'manageProduct.htm')
    else:
        return HttpResponse('You do not have permissions to access this resource.')


class ForAccessories:
    #this display the form for accessories
    def view_accessories_form(request):
        if request.user.is_authenticated:
            return render(request,'accessoriesForm.htm')
        else: 
            return HttpResponse('You do not have permissions to access this resource.')

    #save added accessories
    def save_accessories(request):
        get_name = request.POST['Name']
        get_price = request.POST['Price']
        get_stockNo = request.POST['StockNo']
        get_releaseDate = request.POST['Date']
        get_brand = request.POST['Brand']
        get_description = request.POST['Description']
        get_category = request.POST['Category']

        if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
            image=request.FILES['Image']
            specs=request.FILES['Specification']
            fs1 = FileSystemStorage(location='media/media/images')
            filename1 = fs1.save(image.name, image)
            uploaded_file_url1 = fs1.url(filename1)
            # use this replace command to upload as there seems to be problem with file library
            uploaded_file_url1 = uploaded_file_url1.replace('/media','media/images')

            fs2 = FileSystemStorage(location='media/media/documents')
            filename2 = fs2.save(specs.name,specs)
            uploaded_file_url2 = fs2.url(filename2)
            uploaded_file_url2 = uploaded_file_url2.replace('/media','media/documents')

        productObj = Product.objects.create(name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,brand=get_brand,image=uploaded_file_url1,specs=uploaded_file_url2)
        productObj.save()

        accessoriesObj = Accessories(description=get_description,category=get_category)
        accessoriesObj.save()
        
        return HttpResponse("Successfully Stored !!")

    #To get the inserted number and create context variable and pass to another form
    def get_acc_id(request):
        if request.user.is_authenticated:
            access_id = request.GET['acc_id']
            # print(access_id)
            try:
                accObj = Accessories.objects.get(product_id=access_id)
                context={
                    'acc':accObj
                }
                return render(request,'updateForms/accessoriesUpdate.htm',context)
            except Accessories.DoesNotExist:
                return HttpResponse("ID not found !!")
        else:
            return HttpResponse('You do not have permissions to access this resource.')

        
    #function to update the accessories
    def update_accessories(request,id):
        name=request.POST['Name']
        brand=request.POST['Brand']
        price=request.POST['Price']
        stockNo=request.POST['StockNo']
        date=request.POST['Date']
        description = request.POST['Description']
        category = request.POST['Category']

        updateAccessories = Accessories.objects.get(product_id=id)
        productUpdate = Product.objects.get(id=id)
        productUpdate.name=name
        productUpdate.brand=brand
        productUpdate.price=price
        productUpdate.stockNo=stockNo
        productUpdate.date=date
        updateAccessories.description=description
        updateAccessories.category=category

        # if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
        #     image=request.FILES['Image']
        #     specs=request.FILES['Specification']
        #     fs1 = FileSystemStorage(location='media/media/images')
        #     filename = fs1.save(image.name, image)       
        #     uploaded_file_url2 = fs1.url(filename)
        #     productUpdate.image = uploaded_file_url2.replace('/media','media/images')  

        #     fs2 = FileSystemStorage(location='media/media/documents')
        #     filename2 = fs2.save(specs.name, specs)
        #     uploaded_file_url2 = fs2.url(filename2)
        #     productUpdate.specs = uploaded_file_url2.replace('/media','media/documents')

        updateAccessories.save()
        productUpdate.save()
        return HttpResponse("Successfully Updated !!")

class ForPhones:
    #this display the form to add phone
    def view_phone_form(request):
        if request.user.is_authenticated:
            return render(request,'addPhoneForm.htm')
        else:
           return HttpResponse('You do not have permissions to access this resource.')

    #save retrieved data in database
    def  save_phone_database(request):
        get_screenSize = request.POST['screen size']
        get_RAM = request.POST['ram']
        get_ROM = request.POST['rom']
        get_color = request.POST['Color']
        get_battery = request.POST['Battery']
        get_description = request.POST['Description']
        get_name = request.POST['Name']
        get_price = request.POST['Price']
        get_stockNo = request.POST['StockNo']
        get_releaseDate = request.POST['Date']
        get_brand = request.POST['Brand']
            
        
        if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
            image=request.FILES['Image']
            specs=request.FILES['Specification']
            
            fs1 = FileSystemStorage(location='media/media/images')
            filename1 = fs1.save(image.name, image)
            uploaded_file_url1 = fs1.url(filename1)
            uploaded_file_url1 = uploaded_file_url1.replace('/media','media/images')

            fs2 = FileSystemStorage(location='media/media/documents')
            filename2 = fs2.save(specs.name,specs)
            uploaded_file_url2 = fs2.url(filename2)
            uploaded_file_url2 = uploaded_file_url2.replace('/media','media/documents')

        productObj = Product.objects.create(name=get_name,price=get_price,stockNo=get_stockNo,releaseDate=get_releaseDate,brand=get_brand,image=uploaded_file_url1,specs=uploaded_file_url2)
        productObj.save()

        phoneObj = Phones(screenSize=get_screenSize,RAM=get_RAM,ROM=get_ROM,color=get_color,battery=get_battery,description=get_description)
        phoneObj.save()
        return HttpResponse("Successfully Stored !!")

    #get id to be updated
    def get_phone_id(request):
        if request.user.is_authenticated:
            phoneID = request.GET['phone_id']
            try:
                phoneObj = Phones.objects.get(product_id=phoneID)
                context={'phone':phoneObj}
                return render(request,'updateForms/phoneUpdate.htm',context)
            except Phones.DoesNotExist:
                return HttpResponse("ID not found !!")
        else:
            return HttpResponse('You do not have permissions to access this resource.')

    def update_phones(request,id):
        name=request.POST['Name']
        brand=request.POST['Brand']
        price=request.POST['Price']
        stockNo=request.POST['StockNo']
        date=request.POST['Date']
        description = request.POST['Description']
        category = request.POST['Category']
        ram=request.POST['ram']
        rom=request.POST['rom']
        screenSize = request.POST['screen size']
        color = request.POST['Color']
        battery = request.POST['Battery']

        updatePhone = Phones.objects.get(product_id=id)
        updatePhone.description=description
        updatePhone.category=category
        updatePhone.RAM=ram
        updatePhone.ROM=rom
        updatePhone.screenSize=screenSize
        updatePhone.color=color
        updatePhone.battery=battery

        productUpdate = Product.objects.get(id=id)
        productUpdate.name=name
        productUpdate.brand=brand
        productUpdate.price=price
        productUpdate.stockNo=stockNo
        productUpdate.date=date
        

        # if request.method == 'POST' and (request.FILES['Image'] or request.FILES['Specification']):
        #     image=request.FILES['Image']
        #     specs=request.FILES['Specification']
        #     fs1 = FileSystemStorage(location='media/media/images')
        #     filename = fs1.save(image.name, image)       
        #     uploaded_file_url2 = fs1.url(filename)
        #     productUpdate.image = uploaded_file_url2.replace('/media','media/images')  

        #     fs2 = FileSystemStorage(location='media/media/documents')
        #     filename2 = fs2.save(specs.name, specs)
        #     uploaded_file_url2 = fs2.url(filename2)
        #     productUpdate.specs = uploaded_file_url2.replace('/media','media/documents')

        updatePhone.save()
        productUpdate.save()
        return HttpResponse("Successfully Updated !!")


# *************************************************************************************
# All codes created below this section are done by Ranjan KC
def deleteProducts(request):
    phones = Phones.objects.all()
    accessories = Accessories.objects.all()
    params = {'products':phones}
    return render(request,'delete.html',params)

def confirmDeleteProducts(request,ID):
    product = Phones.objects.get(id=ID)
    product.delete()
    return HttpResponse("Successfully Deleted !!")
