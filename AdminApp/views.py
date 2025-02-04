from itertools import product

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from AdminApp.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import datetime
from WebApp.models import Contact,Register,OrderDB,CartDB
from django.contrib import messages


# Create your views here.

def index(req):
    category = Category.objects.count()
    product = Product.objects.count()
    date = datetime.today()
    return render(req,'index.html',{'category':category,'product':product,'date':date})

def add_category(a):
    date = datetime.today()
    return render(a,'AddCategory.html',{'date':date})

def save_category(b):
    if b.method=='POST':
        c_name = b.POST.get('cname')
        c_desc = b.POST.get('cdesc')
        c_image = b.FILES['cimage']
        obj = Category(C_Name=c_name,C_Desc=c_desc,C_Image=c_image)
        obj.save()
        messages.success(b,'Category Added Successfully..')
        return redirect(add_category)

def display_category(c):
    date = datetime.today()
    cate = Category.objects.all()
    return render(c,'DisplayCategory.html',{'cate':cate,'date':date})

def edit_category(d,c_id):
    date = datetime.today()
    cate = Category.objects.get(id=c_id)
    return render(d,'EditCategory.html',{'cate':cate,'date':date})

def update_category(e,c_id):
    if e.method=='POST':
        c_name = e.POST.get('cname')
        c_desc = e.POST.get('cdesc')
        try:
            img =e.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =Category.objects.get(id=c_id).C_Image
        Category.objects.filter(id=c_id).update(C_Name=c_name,C_Desc=c_desc,C_Image=file)
        messages.success(e,'Category Updated')
        return redirect(display_category)

def del_category(f,c_id):
    del_c = Category.objects.filter(id=c_id)
    del_c.delete()
    messages.error(f,'Category Deleted Successfully')
    return redirect(display_category)


def add_product(g):
    cate = Category.objects.all()
    date = datetime.today()

    return render(g,'AddProduct.html',{'cate':cate,'date':date})

def save_product(h):
    if h.method=='POST':
        pc_name = h.POST.get('pcname')
        p_name = h.POST.get('pname')
        p_quant = h.POST.get('pquant')
        p_price = h.POST.get('pprice')
        p_desc = h.POST.get('pdesc')
        p_image = h.FILES['pimage']
        obj1 = Product(PC_Name=pc_name,P_Name=p_name,P_Quant=p_quant,P_Price=p_price,P_Desc=p_desc,P_Image=p_image)
        messages.success(h,'Product Added Successfully..!')
        obj1.save()
        return redirect(add_product)

def display_product(i):
    prod = Product.objects.all()
    date = datetime.today()

    return render(i,'DisplayProduct.html',{'prod':prod,'date':date})

def edit_product(j,p_id):
    cate = Category.objects.all()
    prod = Product.objects.get(id=p_id)
    date = datetime.today()

    return render(j,'EditProduct.html',{'prod':prod,'cate':cate,'date':date})

def update_product(k,p_id):
    if k.method=='POST':
        pc_name = k.POST.get('pcname')
        p_name = k.POST.get('pname')
        p_quant = k.POST.get('pquant')
        p_price = k.POST.get('pprice')
        p_desc = k.POST.get('pdesc')
        try:
            ime = k.FILES['pimage']
            fse = FileSystemStorage()
            filed = fse.save(ime.name,ime)
        except MultiValueDictKeyError:
            filed = Product.objects.get(id=p_id).P_Image
        Product.objects.filter(id=p_id).update(PC_Name=pc_name,P_Name=p_name,P_Quant=p_quant,P_Price=p_price,P_Desc=p_desc,P_Image=filed)
        messages.success(k,'Updated Successfully')
        return redirect(display_product)

def delete_product(l,p_id):
    del_p = Product.objects.filter(id=p_id)
    del_p.delete()
    messages.error(l,'Product Deleted Successfully')
    return redirect(display_product)

def admin_login_page(log):
    return render(log,'AdminLogin.html')

def admin_login(request):
    if request.method=='POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            var = authenticate(username=un,password=pwd)
            if var is not None:
                login(request,var)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,'Welcome to Admin DashBoard')
                return redirect(index)
            else:
                messages.warning(request,'Invalid Password')
                return redirect(admin_login_page)
        else:
            messages.warning(request,'Invalid Username')
            return redirect(admin_login_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.info(request," You Have Logged Out " )
    return redirect(admin_login_page)


def display_contact(dis):
    date = datetime.today()

    cont = Contact.objects.all()
    return render(dis,'DisplayContact.html',{'cont':cont,'date':date})

def del_contact(con,cont_id):
    del_cont = Contact.objects.filter(id=cont_id)
    del_cont.delete()
    messages.error(con,'Contact Deleted Successfully')
    return redirect(display_contact)

def display_reg_details(regi):
    reg = Register.objects.all()
    date = datetime.today()

    return render(regi,'DisplayRegisterDetails.html',{'reg':reg,'date':date})

def delete_reg_details(regi,reg_id):
    del_reg = Register.objects.filter(id=reg_id)
    del_reg.delete()
    messages.error(regi,'User Deleted Successfully')
    return redirect(display_reg_details)

def view_orders(request):
    date = datetime.today()

    ord = OrderDB.objects.all()
    return render(request,'ShowOrders.html',{'ord':ord,'date':date})

def del_orders(request,o_id):
    order = OrderDB.objects.filter(id=o_id)
    order.delete()
    return redirect(view_orders)

def view_cart(request):
    crt = CartDB.objects.all()
    date = datetime.today()

    return render(request,'CartDetails.html',{'crt':crt,'date':date})

def del_cart(request,cart_id):
    del_cart = CartDB.objects.filter(id=cart_id)
    del_cart.delete()
    return redirect(view_cart)



