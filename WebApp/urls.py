from tkinter.font import names

from django.urls import path
from WebApp import views

urlpatterns = [

    path('Home/',views.home_page,name='Home'),
    path('AboutUs/',views.about,name='AboutUs'),
    path('Contact/',views.contact,name='Contact'),
    path('Save_Contact/',views.save_contact,name='Save_Contact'),
    path('OurProducts/',views.our_products,name='OurProducts'),
    path('FilteredProducts/<fil_prod>/',views.filtered_products,name='FilteredProducts'),
    path('SingleProduct/<int:s_id>',views.single_prod,name='SingleProduct'),


    path('UserLoginPage/', views.user_login_page, name='UserLoginPage'),
    path('', views.user_reg_page, name='UserRegisterPage'),
    path('SaveUserRegister/',views.save_user_reg,name='SaveUserRegister'),
    path('UserLogin/',views.user_login,name='UserLogin'),
    path('UserLogout/',views.user_logout,name='UserLogout'),

    path('Cart_Page/',views.cart_page,name='Cart_Page'),
    path('Save_Cart/',views.save_cart,name='Save_Cart'),
    path('DeleteCart/<int:ct_id>/',views.del_cart,name='DeleteCart'),

    path('CheckOut/',views.cart_checkout,name='CheckOut'),
    path('SaveCheckOut/',views.save_checkout,name='SaveCheckOut'),

    path('PaymentPage/',views.payment_page,name='PaymentPage'),





]