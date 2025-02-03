from django import forms

#if want to use inbuilt function
from django.contrib.auth.forms import UserCreationForm

from .models import Customer


# If you are using a custom user model
#from .models import User

# If using the default User model
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm


class UserCreation_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']    #field to display
        # widgets={
        #     'password':forms.PasswordInput(),
        # }
    


class LoginForm(forms.Form):
    username=forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    password=forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )



class CustomUserForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','country','mobile','zipcode','district']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'district':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'})
            
            
            
        }
        
class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password',widget=forms.PasswordInput(attrs={
        'autofocus':'True','autocomplete':'current-password','class':'form-control'
    }))
    new_password1=forms.CharField(label='New password',widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password','class':'form-control'
    }))
    
    new_password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password','class':'form-control'
    }))
        
        
        
        
        
        
        
        
        
    # Additional fields
    





# from django import forms
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField


# from django.contrib.auth.models import User

# class LoginForm(AuthenticationForm):
#     username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

# class CustomerForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    
#     email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
   
    
#     password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']

