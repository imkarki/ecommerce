from django.db import models

#from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
STATE_CHOICES=(
('kathmandu','kathmandu'),
('pokhara','pokhara'),
('Ramechaap','Ramechhap'),
('Lalitpur','Lalitpur'),
('Bhaktapur','Bhaktapur'),
)




CATEGORY_CHOICES=(
    ('CK','Cake'),
    ('IC','Ice-Cream'),
    ('CF','Coffee'),
)
#uploading any image in admin panel upload the image in media directory
class Products(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    # composition=models.TextField(default='')
    # prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    #product_image=models.ImageField(upload_to='things/')
    
    product_image = CloudinaryField('image')  # Replaces ImageField

    
    def __str__(self):
        return self.title
    
    

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    country=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    district=models.CharField(choices=STATE_CHOICES,max_length=100)
    
    def __str__(self):
        return self.name
    
        
    
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    class meta:
        unique_together=('user','product')
    
        
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
    

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    e_id=models.CharField(max_length=100,blank=True,null=True)  # Transaction ID
    e_status=models.CharField(max_length=100,blank=True,null=True)  #esewa status
    e_payment=models.CharField(max_length=100,blank=True,null=True)  #esewa response
    paid=models.BooleanField(default=False)
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed',"Packed"),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
 
    
class OrderPlaced(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=40,choices=STATUS_CHOICES,default="Pending")
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    
    @property
    
    def total_cost(self):
        return self.quantity * self.product.discount_price

#it is used to store messages send by the customer 
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
  
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject


   
    

