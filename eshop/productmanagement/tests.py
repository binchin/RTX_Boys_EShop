from django.test import TestCase
from .models import Product, Phones, Laptop, Accessories
# Create your tests here.

class ProductTest(TestCase):
    def setUp(self):
        a1 = Product.objects.create(name="iPhone 11 Pro 64GB",stockNo="20", price="157000",releaseDate="2019-11-06",brand="apple",specs="/media/documents/specification_66GrQDO_aZQkyuZ.pdf",image="/media/images/iphone-11-pro-64gb.jpeg")
        a2 = Product.objects.create(name="iPhone X 64GB Silver",stockNo="8", price="146000",releaseDate="2018-09-13",brand="apple",specs="/media/images/iphone-x_64gb_silver_DVi4pJJ.jpg")

    def test_count_product_in_stock(self):
        prod= Product.objects.all()
        self.assertEqual(prod.count(), 2)

    def test_product_stock(self):
        p1 = Product.objects.create(name="iPhone 11 Pro 64GB",stockNo="20", price="157000",releaseDate="2019-11-06",brand="apple",specs="/media/documents/specification_66GrQDO_aZQkyuZ.pdf",image="/media/images/iphone-11-pro-64gb.jpeg")
        self.assertTrue(p1.is_in_stock())
