from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 255)
    price = models.IntegerField()
    stockNo = models.IntegerField()
    releaseDate = models.DateField(auto_now=False)
    specs = models.FileField(upload_to='media/media/documents/')
    image = models.ImageField(upload_to='media/media/images/')
    brand = models.CharField(max_length=255)
    
    def __str__(self):
        return (self.name)
    #abstract model which allows inheritance and the table is not created
    # class Meta:
    #     abstract = True
    # ordering = ["name","price","stockNo","releaseDate","specs","brand","image"]

class Phones(models.Model):
    screenSize = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    RAM = models.CharField(max_length=255)
    ROM = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)
    description = models.TextField() 
    product  = models.OneToOneField(Product,on_delete=models.CASCADE, primary_key = True)
    def __str__(self):
        return str(self.id)


class Accessories(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE, primary_key = True)
    category = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return str(self.id)

class Laptop(models.Model):
    product  = models.OneToOneField(Product,on_delete=models.CASCADE, primary_key = True)
    screenSize = models.CharField(max_length=255)
    color = models.CharField(max_length=60)
    RAM = models.CharField(max_length=255)
    ROM = models.CharField(max_length=255)
    battery = models.CharField(max_length=60)
    cpu = models.CharField(max_length=255)
    graphics = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    description = models.TextField() 
    def __str__(self):
        return str(self.id)
