from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    brand = models.CharField(max_length=255,null=True, blank=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating= models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    numReviews = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 255, null=True,blank=True)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.rating)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL,null=True)
    paymentMethod = models.CharField(max_length=255)
    taxPrice =models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    shoppingPrice =models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    isDeliverd =  models.BooleanField(default=False)
    deliverd_at = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return str(self.created_at)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    qty = models.IntegerField(blank=True, null=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    # image=
    _id = models.AutoField(primary_key=True, editable=False)
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete = models.SET_NULL, null=True, blank=True)
    address =models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    countery  = models.CharField(max_length=255, null=True, blank=True)
    shoppin_price =models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    
    def __str__(self) -> str:
        return str(self.name)