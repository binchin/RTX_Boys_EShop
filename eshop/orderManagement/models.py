from django.db import models
from productmanagement.models import *
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    orderID = models.IntegerField()
    # phone = models.ManyToManyField(Phones, blank=True)
    # accessories = models.ManyToManyField(Accessories, blank=True)
    product = models.ManyToManyField(Product,blank=True)
    customer = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return f"{self.orderID} is ordered by {list(self.customer.all())} which contains {list(self.product.all())}"
    