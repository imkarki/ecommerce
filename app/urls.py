from django.contrib import admin
from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings

#for the login form auth_view is important
from django.contrib.auth import views as auth_view

from .forms import MyPasswordChangeForm

from django.contrib.auth.views import LogoutView

#from .forms import LoginForm

from .views import MyPasswordReset,MyPasswordConfirm

from .views import ManageCartView

from .views import search

#to change the name of the admin
from django.contrib import admin

#choice ma text xa so use slug
urlpatterns = [
    path("",views.index,name="index"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("product-all/<int:pk>",views.ProductAll.as_view(),name="product-all"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="CategoryTitle"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    
    #authentication
    #path("regist/",views.register_view,name="register"),
    
    
    #login authentication
    #path('registration/',views.CustomerRegistration.as_view(),name='registration'),
    
    path('registration/',views.register_view,name='registration'),
    
    #path('success/',views.success_view,name='success'),
    
    path('loginview/',views.login_view,name="login_views"),
    
    path('profile/',views.profile.as_view(),name="profile"),     #detail
    
    path('detail',views.detail,name='detail'),             #address
    
    path('update/<int:pk>',views.update_profile.as_view(),name="update"),
    
    
    # path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    
    # path('password-reset/',auth_view.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=MyPasswordResetForm),name='password_reset')
    
    path('add-to-cart/',views.add_to_carts,name='add-to-cart'),
    
    path('cart/',views.show_cart,name='showcart'),
    
    #path('manage-cart/<int:pro_id>/',ManageCartView.as_view(),name="managecart"),
    
    path('manage-cart/<int:cp_id>/',ManageCartView.as_view(),name='managecart'),
    
    #for the checkout
    path('checkout/',views.checkout.as_view(),name="checkout"),
    
    
    
    #correct
    #path("esewa-request/",views.esewarequest,name='esewarequest'),
    
    

    
    #ordered placed
    path('order/',views.orders,name="orders"),
    
    #search
    path('search/',search,name="search"),
    
    
    #password change Authetication 
    path('password-change/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name="passwordchange"),
    
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchanged.html'),name='passwordchangedone'),
    
    #for logout
    #path('logout/',auth_view.LogoutView.as_view(next_page='login_views'),name='logout'),
    
    path('logout/',views.logout,name='logout'),
    
    
    #for most important things like reset password sending the link to email
    #name="..." yo vitra ko name haru sab pre defined built in ho so don't change it  
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name="app/passwordreset.html",form_class=MyPasswordReset),name='password_reset'),
    
    path('password-reset-done/',auth_view.PasswordResetDoneView.as_view(template_name='app/passwordreset_done.html'),name='password_reset_done'),
    
    
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_confirm.html',form_class=MyPasswordConfirm),name='password_reset_confirm'),
    
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/passwordcomplete.html'),name='password_reset_complete'),
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header="AK ecommerce"
admin.site.site_title="AK ecommerce"
admin.site.site_index_title="Welcome to AK mini business"