from django.shortcuts import render,redirect

from django.views import View
from .models import Products

from django.db.models import Count



from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout


#from .forms import RegistrationForm


from .forms import UserCreation_form


from . import forms
# from django.contrib.auth.views import LoginView
#to import from forms.py classname
from .forms import LoginForm,CustomUserForm


#for login form 
from django.contrib.auth import authenticate,login

from .models import Customer
# Create your views here.


# for the logout
from django.contrib.auth import logout

from django import forms

from django.contrib.auth.forms import SetPasswordForm,PasswordResetForm

from django.contrib.auth.decorators import login_required

from .models import Carts

from django.http import HttpResponseBadRequest


#for the payment 
import hashlib
import uuid
from django.conf import settings
from django.shortcuts import render
from .models import Carts,Payment,OrderPlaced
import hmac

import base64
from django.conf import settings

from django.contrib.auth.decorators import login_required

import logging #for debugging 

from django.contrib.auth.models import User

from django.db.models import Sum

# for search
from django.db.models import Q

#for class
from django.utils.decorators import method_decorator

from django.utils.html import format_html
from django.urls import reverse

#messages from the customer
from . models import ContactMessage

#for email
from django.core.mail import send_mail
from django.conf import settings

#for payment integration
from esewa import EsewaPayment,generate_signature

from django.http import JsonResponse

import requests

import uuid
import hmac
import hashlib
import base64
from esewa.signature import generate_signature  # Import the function


@login_required
def index(request):
    a=Carts.objects.filter(user=request.user)
    car_count=a.count()
    return render(request,'app/home.html',{"car_count":car_count})

# def products(self, obj):
#     if obj.product:  # Ensure product exists
#         link = reverse("admin:app_product_change", args=[obj.product.pk])
#         return format_html('<a href="{}">{}</a>', link, obj.product.title)
#     return "-"


@login_required
def about(request):
    car_count=0
    a=Carts.objects.filter(user=request.user)
    car_count=a.count()
    return render(request,"app/about.html",locals())

# @login_required
# def contact(request):
#     car_count=0
#     a=Carts.objects.filter(user=request.user)
#     car_count=a.count()
#     return render(request,"app/contact.html",locals())




#can use class or function
#get-to show data post-to perform the action


# class CategoryView(View):
    
#     def get(self,request,val):
#         product= Products.objects.filter(category=val)
#         title=Products.objects.filter(category=val).values('title').annotate(total=Count('title'))
#         return render(request,'app/category.html',locals())
    
@method_decorator(login_required,name='dispatch')    
class CategoryView(View):
    def get(self, request, val):
        product = Products.objects.filter(category=val)
       
        title = Products.objects.filter(category=val).values('title').annotate(total=Count('title'))
        
        # Calculate cart count only if the user is authenticated
        car_count = len(Carts.objects.filter(user=request.user)) if request.user.is_authenticated else 0
        
        return render(request, 'app/category.html', {'product': product, 'title': title, 'car_count': car_count})

@method_decorator(login_required,name='dispatch')   
class ProductAll(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        car_count=Carts.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
        return render(request,"app/productall.html",{'product':product,'car_count':car_count})
    
@method_decorator(login_required,name='dispatch')      
class CategoryTitle(View):
    def get(self,request,val):
        product=Products.objects.filter(title=val)
        title=Products.objects.filter(category=product[0].category).values('title')
        car_count=Carts.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
        return render(request,"app/category.html",{'product':product,'title':title,'car_count':car_count})
        

# class CustomerRegistration(View):
#     def get(self,request):
#         form=CustomerForm()
#         return render(request,'app/customerregistration.html',locals())
    
#     def post(self,request):
#         form=CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'User Register Successfully')
#         else:
#             messages.warning(request,"Invalid Input Data")
#         return render(request,"app/customerregistration.html",locals())
    
# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Save user
#             messages.success(request, 'Registration successful! You can log in.')
#             login(request, user)  # Log in the user automatically
#             return redirect("success")  # Redirect to success page
#         else:
#             print(form.errors)  # debug :print errors if form is invalid 
#     else:
#         form = UserCreationForm()  # Ensure form is initialized for GET request

#     return render(request, 'app/customerregistration.html', {'form': form})  # Pass form to template   
    
    

def register_view(request):
    if request.method=="POST":
        form=UserCreation_form(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Registration successflly! you can log in')
            login(request,user)   #login in the user automatically
            # return redirect("success")  #redirect to a success page
            return redirect("login_views")
        
    else:
        form=UserCreation_form()
        
    # if request.method=='POST':
    #     form=UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user=form.save()
    #         login(request,user)
    #         return 'success'
    #     else:
    #         form=UserCreationForm()
    return render(request,'app/customerregistration.html',{'form':form})    #,{'form':form}

# def get(self,request):
#     form=UserCreation_form()
#     return render(request,'app/customerregistration.html',locals())

#@login_required
def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('profile')   #replace with your desired url
            else:
                form.add_error(None,"Invalid username or password")
                
    else:
        form=LoginForm()
    
    return render(request,'app/login.html',{'form':form})


#detail
@method_decorator(login_required,name='dispatch')   
class profile(View):
    def get(self,request):
        form=CustomUserForm()
        car_count=0
        a=Carts.objects.filter(user=request.user)
        car_count=a.count()
        
        #form=CustomerUserForm()
        return render(request,'app/profile.html',{'form':form,'car_count':car_count})
    
    def post(self,request):
        form=CustomUserForm(request.POST)
        car_count=0
        a=Carts.objects.filter(user=request.user)
        car_count=a.count()
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            country=form.cleaned_data['country']
            mobile=form.cleaned_data['mobile']
            district=form.cleaned_data['district']
            zipcode=form.cleaned_data['zipcode']
            
            #create the object for above and save it
            
            object=Customer(user=user,name=name,locality=locality,country=country,mobile=mobile,district=district,zipcode=zipcode)
            object.save()
            messages.success(request,"congratulation! profile saved successfully")
            return redirect('profile')
        else:
            messages.warning(request,"Invalid Input Data")
        
        return render(request,'app/profile.html',locals())
        
        

#detail=address
@login_required
def detail(request):
    form=Customer.objects.filter(user=request.user)
    car_count=0
    a=Carts.objects.filter(user=request.user)
    car_count=a.count()
    
    
    return render(request,'app/mydetail.html',locals())



@method_decorator(login_required,name='dispatch')   
class update_profile(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomUserForm(instance=add)
        return render(request,'app/update.html',locals())
    def post(self,request,pk):
        form=CustomUserForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.country=form.cleaned_data['country']
            add.mobile=form.cleaned_data['mobile']
            add.district=form.cleaned_data['district']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulation for successfull updates")
        else:
            messages.warning(request,"sorry something went wrong fill properly")
        return render(request, 'app/update.html', locals())
        
    

def logout(request):
    # logout(request)
    return render(request,'app/logout.html')
    

#reset 
class MyPasswordReset(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label="Email Address",max_length=254,)  
    

#email uid form 
class MyPasswordConfirm(SetPasswordForm):
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    new_password1=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    
    
    

    
#Add to Cart
@login_required
def add_to_carts(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    try:
        product_id = int(product_id.rstrip("/"))  # Remove trailing slash and convert to integer
    except ValueError:
        return HttpResponseBadRequest("Invalid Product ID")
    products=Products.objects.get(id=product_id)
    Carts(user=user,product=products).save()
    
    
    return redirect("/cart")  #("cart/") yo garda problem face hunxa in it 
    
    #return render(request,'app/cart_add.html',locals())  #gives empty otuptu

@login_required
def show_cart(request):
    user=request.user
    cart=Carts.objects.filter(user=user)
    amount=0
    
    value = 0  # Initialize value to avoid UnboundLocalError
  
    for a in cart:
        value=a.quantity * a.product.discount_price
        amount=amount+value
    totalamount=amount+40
    car_count=len(Carts.objects.filter(user=request.user).values('quantity')) if request.user.is_authenticated else 0
    #car_count = Carts.objects.filter(user=request.user).annotate(total_quantity=Sum('quantity'))

    
    
    #these two variables are passed through the locals 
    return render(request,'app/cart_add.html',{'cart':cart,"value":value,"amount":amount,"cart":cart,"totalamount":totalamount,"car_count":car_count})
    
@method_decorator(login_required,name='dispatch')   
class ManageCartView(View):
    def get(self,request,*args , **kwargs):
        print("This is manage cart section")
        cp_id=self.kwargs['cp_id']   #we got cp_id here 
        action=request.GET.get("action")   #this action is defined in a html file of +,-,remove
        
        cpid=self.kwargs.get('cp_id',None)
        print(f"Action:{action},cart_product id:{cpid}")
        
        co_obj=Carts.objects.get(id=cp_id)
        # cart_obj=co_obj.cart   #it would be requrired for child under cartprodcut another foreign cart if defined
        
        if action=="dcr":
            co_obj.quantity+=1
            co_obj.rate = co_obj.quantity * co_obj.product.selling_price  # Update rate dynamically
            co_obj.save()
        elif action=="inc":
            if co_obj.quantity > 1:
                co_obj.quantity -= 1
                co_obj.rate = co_obj.quantity * co_obj.product.selling_price  # Update rate dynamically
                co_obj.save()
            else:
                co_obj.delete()  #remove the cart item if quantity is 0 

        elif action=="rmv":
            co_obj.delete()   #remove the cart item 
            print(f"Action: {action}, Cart ID: {co_obj}")

        else:
            pass
        print(cp_id,action)
        return redirect("/cart")   #redirect to same page as before
    
@method_decorator(login_required,name='dispatch')    
class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        # carts=Carts.objects.all()
        carts=Carts.objects.filter(user=user)
        
        totamount=0
        for a in carts:
            value=a.quantity * a.product.discount_price
            totamount=totamount+value
        totalamount=totamount+40   #adding delivery charge
        
        
        car_count=len(Carts.objects.filter(user=request.user)) if request.user.is_authenticated else 0
        
        #e_id=uuid.uuid4()  #Generate a unique transaction ID
        
        return render(request,'app/checkout.html',{"add":add,"carts":carts,"totamount":totamount,"totalamount":totalamount,"car_count":car_count})
        
        #return render(request,'app/home.html',{"add":add,"carts":carts,"totamount":totamount,"totalamount":totalamount,"car_count":car_count})
    
    # def post(self,request):
    #     user=request.user
    #     amount=request.POST.get('amount')
    #     e_id=request.POST.get('transaction_uuid')
        
    #     #save payment information before redirecting to esewa
    #     payment=Payment.objects.create(user=user,amount=amount,e_id=e_id,paid=False)
    #     payment.save()
        
    #     #return redirect('esewarequest')
    #     return redirect('/')
    




     

# @login_required
# def orders(request):
#     user = User.objects.get(username="carkey")  # Replace with a real username
    
#     order_placed=OrderPlaced.objects.filter(user=user)  # Only logged-in user's orders
    
#     for order in order_placed:
#         print(order.id)
    
#     return render(request,'app/ordered.html',{'ordered_placed':order_placed})


@login_required
def orders(request):
    if request.user.is_superuser:  # Example: Show all orders if the user is an admin
        order_placed = OrderPlaced.objects.all()
    else:
        order_placed = OrderPlaced.objects.filter(user=request.user)  # Orders only for the logged-in user
    
    return render(request, 'app/ordered.html', {'ordered_placed': order_placed})


#search
@login_required
def search(request):
    
    query=request.GET.get('search','')# Use .get() to avoid KeyError
    
    products = Products.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)) if query else []
    
    return render(request,"app/search.html",locals())



def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        
        subject = f"Message from {name}"
        message_content = f"Message: {message}\n\nFrom: {name} ({email})"
        from_email = email
        to_email = settings.EMAIL_HOST_USER  # Send to your email

            # Send the email
        send_mail(subject, message_content, from_email, [to_email])

            # Display a success message to the user
        messages.success(request, 'Your message has been sent successfully!')
        
    return render(request,'app/contact.html')
        
        


   
        #correct

# SECRET_KEY = "8gBm/:&EnhH.1/q"
# CALLBACK_URL = "https://developer.esewa.com.np/success"
# PRODUCT_CODE = "EPAYTEST"     
   #correct   
     
def esewarequest(request):
    if request.method=="POST":
       
        user=request.user
        amount=request.POST.get("amount")
        #transaction_uuid=str(uuid.uuid4()) #unique transaction ID
        
        transaction_uuid=str(uuid.uuid4())[:8] #unique transaction ID with smaller length
        
        #Create a new payment record
        payment = Payment.objects.create(
            user=user,
            amount=amount,
            e_id=transaction_uuid,
            e_status="Pending"
        )
        
        
        
    
        epayment = EsewaPayment(
            success_url=f'http://localhost:8000/esewa-success/{payment.id}',
            failure_url=f'http://localhost:8000/esewa-failure/{payment.id}'
        )
        epayment.create_signature(amount, transaction_uuid)
        payment.save()

        
        context={
            
            'amount':amount,
            'form':epayment.generate_form()
        }
        return render(request,"app/esewarequest.html",context) 
    return redirect("checkout/")  #redirect to checkout if accessed directly   

def esewa_success(request,id):
    payment = Payment.objects.get(id=id)
    transaction_uuid = payment.e_id
    amount = payment.amount
    epayment = EsewaPayment()
    epayment.create_signature(amount, transaction_uuid)
    if epayment.is_completed(dev=True):
        e_status = "Accepted"
        payment.e_status = e_status
        payment.save()
        
        return render(request, "app/payment_success.html", {"transaction_id": transaction_uuid})
    else:
        return render(request, "app/payment_failed.html")   

    
def esewa_failure(request):
    return render(request, "app/payment_failed.html")

        





    

