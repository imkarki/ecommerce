from django.contrib import admin
from . models import Products,Customer,Carts,Payment,OrderPlaced


#to provide the direct link in models.py
from django.utils.html import format_html
from django.urls import reverse

from django.contrib.auth.models import Group
# Register your models here.

from . models import ContactMessage

@admin.register(Products)
class ProductModel(admin.ModelAdmin):
    list_display=['id','title','discount_price','category','product_image','selling_price']
    
    
@admin.register(Customer)
class CustomerModel(admin.ModelAdmin):
    list_display=['id','user','locality','country','district','zipcode']
    

@admin.register(Carts)
class CartsModel(admin.ModelAdmin):
    list_display=['id','user','products','quantity'] #change inside list product to function name product
    def products(self,obj):   #used to create the link in database when clicked take you to the detail
        link=reverse("admin:app_products_change",args=[obj.product.pk])  #this take much time be careful (admin:appname_functionname_change)
        print(link)
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    
@admin.register(Payment)
class PaymentModel(admin.ModelAdmin):
    list_display=['id','user','amount','e_id','e_status','e_payment','e_status']
    
@admin.register(OrderPlaced)
class OrderPlacedModel(admin.ModelAdmin):
    list_display=['id','user','customers','products','quantity','ordered_date','status','payment']
    
    def customers(self,obj):   #used to create the link in database when clicked take you to the detail
        link=reverse("admin:app_customer_change",args=[obj.customer.pk])  #this take much time be careful (admin:appname_functionname_change)
        print(link)
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)
    
    
    def products(self,obj):   #used to create the link in database when clicked take you to the detail
        link=reverse("admin:app_products_change",args=[obj.product.pk])  #this take much time be careful (admin:appname_functionname_change)
        print(link)
        return format_html('<a href="{}">{}</a>',link,obj.product.title)
    
    
    
#to remove the group here 
admin.site.unregister(Group)

#to send the messages from the customer 
admin.site.register(ContactMessage)
