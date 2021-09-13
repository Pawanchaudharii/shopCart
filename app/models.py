from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Max
from django.db.models.fields import FloatField
from django.db.models.deletion import CASCADE
from AdminApp.models import ElectronicsProduct, FashionProduct

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default="")

    class Meta:
        db_table = "UserInfo"

    def __str__(self):
        return self.username

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=CASCADE)
    eleproduct = models.ForeignKey(ElectronicsProduct, on_delete=CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"

    def __str__(self):
        return self.user

class MyCart1(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=CASCADE)
    fashionproduct = models.ForeignKey(FashionProduct, on_delete=CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart1"

    def __str__(self):
        return self.user

class Profile(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()

    class Meta:
        db_table = "Profile"

    def __str__(self):
        return self.name

class Payment(models.Model):
    card_no =  models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry = models.CharField(max_length=7)
    balance = models.FloatField(default=10000)

    class Meta:
        db_table = "Payment"

    def __str__(self):
        return self.card_no

class Order(models.Model):
    order_date = models.DateField()
    user = models.ForeignKey(UserInfo, on_delete=CASCADE)
    amount = models.FloatField(default=100)
    order_details = models.CharField(max_length=400)
    
    class Meta:
        db_table = "Order"    

    def __str__(self):
        return self.order_details
