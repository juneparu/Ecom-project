from django.db import models
import datetime

class Category(models.Model):
    name= models.CharField(max_length=50)
    
    def _str_(self):
       return self.name 
   
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def _str_(self):
       return f'{self.first_name} {self.last_name}'
   
   
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0, decimal_places=2 , max_digits=6)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=250, default='', blank=True ,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    
    def _str_(self):
       return self.name
   
class Order(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE )
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE )
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100, default='',blank=True  )
    phone=models.CharField(max_length=20, default='', blank=True )
    date=models.DateField(default=datetime.datetime.today  )
    status=models.BooleanField(default=False)
    
    def _str_(self):
       return self.product
 
# class Wishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class WishlistItem(models.Model):
#     wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('wishlist', 'product') 

# Create your models here.
class wishlistmodel(models.Model):
    is_checked = models.BooleanField(default=False)
    wishlist = models.CharField(max_length=50)