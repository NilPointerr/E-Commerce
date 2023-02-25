from django.shortcuts import render, HttpResponse, redirect, HttpResponsePermanentRedirect, HttpResponseRedirect
from datetime import datetime
from home.models import Contact, Login, Product,Orders
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.views.generic import ListView


def homepage(request):
    # if request.Logins.is_anonymous:
    #     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    #     return redirect('login')
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
 

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_no = request.POST['mobile']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email,
                          mobile_no=mobile_no, desc=desc)
        contact.save()
        messages.success(request, 'Youe message hase been sent succesfully...')

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


def service(request):
    return render(request, 'category.html')
    # return HttpResponse("this is service page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def register_1(request):
    if request.method =="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]

        if password ==re_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already exist")
                return render (request, 'register.html') 

            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email already Exist!")
                return render (request, 'register.html') 

            else:            
                user = User.objects.create_user(first_name = first_name,last_name = last_name,
                        username=username,email = email,password = password)
                user.save()
                return redirect('login')
        else:
            messages.error(request,"Password Does not march!")
            return render (request, 'register.html') 

    else:
        return render (request, 'register.html')  

def loginuser(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        password = request.POST['password']
        login = Login(Name=Name, password=password)
        login.save()
        messages.success(request, 'your login is succesfull')
        user = authenticate(username=Name, password=password)
        if user is None:
            return redirect(homepage)
            # A backend authenticated the credentials
        else:   
            return render(request, 'login.html')
        #      # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('')


def mobiles(request):
    return render(request, 'mobiles.html')
    # return HttpResponse("this is about page")


def laptop(request):
    pro = Product.objects.all()
    display = {'info': pro}

    return render(request, 'laptop.html', display)


class login_detail(ListView):
    template_name = 'login_detail.html'
    model = Login

# def viewdata(request):
#     login_de = Login.objects.all()
#     print(login_de)
#     new = {'data': login_de}
#     return render(request, 'temp.html', new)


def product_desc(request,myid):
    pro = Product.objects.filter(product_id = myid)
    detail = {'Prod':pro}
    return render(request, 'product_desc.html',detail)


# def cart(request):
#     return render(request, 'cart.html')

def cart(request):
    if request.method == "POST":
         items_Json= request.POST["items_Json"]
         name=request.POST["name"]
         email=request.POST["email"]
         address1=request.POST["address1"] 
         address2 = request.POST["address2"]
         city=request.POST["city"]
         state=request.POST["state"]
         zip_code=request.POST["zip_code"]
         phone=request.POST["phone"]

         order = Orders(items_Json= items_Json, name=name, email=email, address1= address1, address2 = address2 , city=city, state=state, zip_code=zip_code, phone=phone)
         order.save()
         print("$$$$$$$$$$$$$$$$$$$$$$$")
         thank=True
         id=order.order_id
         return render(request, 'cart.html', {'thank':thank, 'id':id})
    return render(request, 'cart.html')

    
