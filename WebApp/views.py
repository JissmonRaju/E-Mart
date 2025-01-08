import razorpay
from django.shortcuts import render, redirect
from django.template.context_processors import request

from AdminApp.models import Category, Product
from WebApp.models import Contact,Register,CartDB,OrderDB
from django.contrib import messages


# Create your views here.

def home_page(request):
    categ = Category.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'Home.html', {'categ': categ,'x':x})


def about(request):
    categ = Category.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'AboutUs.html', {'categ': categ,'x':x})


def contact(request):
    categ = Category.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'Contact.html', {'categ': categ,'x':x})


def save_contact(d):
    if d.method == 'POST':
        c_name = d.POST.get('name')
        c_email = d.POST.get('email')
        c_msg = d.POST.get('msg')
        obj = Contact(Name=c_name, Email=c_email, Message=c_msg)
        obj.save()
        messages.success(d,'Your Messages Submitted Successfully')
        return redirect(contact)


def our_products(request):
    categ = Category.objects.all()
    produ = Product.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'OurProducts.html', {'categ': categ, 'produ': produ,'x':x})


def filtered_products(request, fil_prod):
    categ = Category.objects.all()
    produ = Product.objects.all()
    pro = Product.objects.filter(PC_Name=fil_prod)
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'Filtered_Products.html', {'pro': pro, 'categ': categ, 'produ': produ,'x':x})


def single_prod(request, s_id):
    sing = Product.objects.get(id=s_id)
    categ = Category.objects.all()
    produ = Product.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    return render(request, 'SingleProduct.html', {'sing': sing, 'categ': categ, 'produ': produ,'x':x})


def user_login_page(request):
    return render(request, 'UserLogin.html')


def user_reg_page(request):
    return render(request, 'UserRegister.html')


def save_user_reg(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_mail = request.POST.get('usermail')
        user_mobile = request.POST.get('usermobile')
        pass_word = request.POST.get('userpass')
        con_pass = request.POST.get('confirmpass')
        obj = Register(User_Name=user_name, Email=user_mail, Mobile=user_mobile, PassWord=pass_word,
                       Confirm_Password=con_pass)
        obj.save()
        messages.success(request,'Registered Successfully')
        return redirect(user_login_page)


def user_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('uname')
        pwd = request.POST.get('pass')
        if Register.objects.filter(User_Name=u_name,PassWord=pwd).exists():
            request.session['User_Name']=u_name
            request.session['PassWord']=pwd
            messages.success(request,'Login Success')

            return redirect(home_page)
        else:
            return redirect(user_login_page)
    else:
        return redirect(user_login_page)

def user_logout(request):
    del request.session['User_Name']
    del request.session['PassWord']
    messages.info(request," You Have Logged Out " )
    return redirect(home_page)


def cart_page(request):
    sub_total = 0
    ship_charge = 0
    total = 0
    categ = Category.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    crt = CartDB.objects.filter(User_Name=request.session['User_Name'])
    for i in crt:
        sub_total += i.Total
        if sub_total<1000:
            ship_charge = 100
        else:
            ship_charge = 0
        total = sub_total + ship_charge

    return render(request, 'Cart.html',{'categ': categ,'crt':crt,'sub_total':sub_total,'ship_charge':ship_charge,'total':total,'x':x})

def save_cart(request):
    if request.method=='POST':
        p_name = request.POST.get('pname')
        p_qty = request.POST.get('quant')
        p_price = request.POST.get('price')
        p_total = request.POST.get('total')
        user_name = request.POST.get('username')
        try:
            x = Product.objects.get(P_Name=p_name)
            img = x.P_Image
        except Product.DoesNotExist:
            img = None
        obj = CartDB(
            User_Name=user_name,
            Product_Name=p_name,
            Quantity=p_qty,
            Price=p_price,
            Total=p_total,
            Product_Image=img)

        obj.save()
        messages.success(request,'Added To Cart')
        return redirect(home_page)
        
def del_cart(request,ct_id):
    d_cart = CartDB.objects.filter(id=ct_id)
    d_cart.delete()
    messages.warning(request,'Removed From Cart')
    return redirect(cart_page)


def cart_checkout(request):
    sub_total = 0
    ship_charge = 0
    total = 0
    categ = Category.objects.all()
    cart_count = CartDB.objects.filter(User_Name=request.session['User_Name'])
    x = cart_count.count()
    crt = CartDB.objects.filter(User_Name=request.session['User_Name'])
    for i in crt:
        sub_total += i.Total
        if sub_total<1000:
            ship_charge = 100
        else:
            ship_charge = 0
        total = sub_total + ship_charge
    return render(request,'CheckOut.html',{'categ': categ,'crt':crt,'sub_total':sub_total,'ship_charge':ship_charge,'total':total,'x':x})

def save_checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        mobile = request.POST.get('mobile')
        mail = request.POST.get('mail')
        total = request.POST.get('total')
        msg = request.POST.get('message')

        obj = OrderDB(Name=name,Email=mail,
                      Place=place,Address=address,
                      Mobile=mobile,State=state,
                      Pin=pin,Total_Price=total,
                      Message=msg)
        obj.save()
        return redirect(payment_page)

def payment_page(request):
    nm = OrderDB.objects.order_by('-id').first()

    pay = nm.Total_Price    #fetching total price

    amt = int(pay*100)      #converting to smallest currency unit (paisa)

    pay_str = str(amt)      #reconverting to string

    if request.method=='POST':
        ord_currency = 'INR'
        client = razorpay.Client(auth=('2D7FeodPxKgqIiWZDYhkNc7L','rzp_test_qtgRvY4PWS4ZIy'))
        payment = client.order.create({'amount':amt,'currency':ord_currency})


    return render(request,'PaymentPage.html',{'nm': nm,'pay_str':pay_str})
