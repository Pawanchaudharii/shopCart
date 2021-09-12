from django.db.models.deletion import CASCADE
from shopCart.settings import DATABASES
from django.db import models

# Create your models here.
class Electronics(models.Model):
    ele_name = models.CharField(max_length=20)

    class Meta:
        db_table = "Electronics"

    def __str__(self):
        return self.ele_name

class Fashion(models.Model):
    fashion_name = models.CharField(max_length=20)

    class Meta:
        db_table = "Fashion"

    def __str__(self):
        return self.fashion_name

class ElectronicsProduct(models.Model):
    electronicsproductname = models.CharField(max_length=50)
    electronicsproduct_image = models.ImageField(default="abc.jpg", upload_to="images")
    price = models.FloatField(default=100)
    description = models.CharField(max_length=10000)
    electronics = models.ForeignKey(Electronics, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "ElectronicsProduct"

    def __str__(self):
        return self.electronicsproductname

class FashionProduct(models.Model):
    fashionproductname = models.CharField(max_length=50)
    fashionproduct_image = models.ImageField(default="abc.jpg", upload_to="images")
    price = models.FloatField(default=100)
    description = models.CharField(max_length=10000)
    fashion = models.ForeignKey(Fashion, on_delete=models.CASCADE)

    class Meta:
        db_table = "FashionProduct"

    def __str__(self):
        return self.fashionproductname

# Username (leave blank to use 'pavan-pc'): shopCart
# Email address: shopCart@gmail.com
# Password: pawan
# Password (again): pawan123