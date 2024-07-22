from django.db import models
from django.contrib.auth.models import User


import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 
   
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
       return f'{self.first_name} {self.last_name}'
   
   
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2 , max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity=models.IntegerField(default=1)
    description=models.CharField(max_length=250, default='', blank=True ,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    
    def __str__(self):
       return self.name
   
class Order(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE )
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE )
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100, default='',blank=True  )
    phone=models.CharField(max_length=20, default='', blank=True )
    date=models.DateField(default=datetime.datetime.today  )
    status=models.BooleanField(default=False)
    
    def __str__(self):
       return self.Product
 
class wishlist(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE ,default=1 )
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE, default=1 )
    quantity=models.IntegerField(default=1)
    date_added = models.DateTimeField(default=datetime.datetime.today )
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.Customer} - {self.Product}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None ) 
    
    def get_total(self):
        return self.quantity * self.product.price
    
    