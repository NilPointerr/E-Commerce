from django.shortcuts import render,HttpResponse,redirect,HttpResponsePermanentRedirect , HttpResponseRedirect
from datetime import datetime
from home.models import Contact,Login,Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout

def homepage(request):
    # if request.Logins.is_anonymous:
    #     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    #     return redirect('login')     
    return render(request,'index.html')
    # return HttpResponse("this is homepage")
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_no = request.POST['mobile']
        desc = request.POST['desc']
        contact = Contact(name=name,email= email,mobile_no = mobile_no,desc = desc )
        contact.save()
        messages.success(request, 'Youe message hase been sent succesfully...')


    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
def service(request):
    return render(request,'category.html')
    # return HttpResponse("this is service page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is about page")
def loginuser(request):
    if request.method =='POST':
        Name = request.POST['Name']
        password = request.POST['password']
        login =Login(Name = Name, password = password)
        login.save()    
        messages.success(request, 'your login is succesfull')
        user = authenticate(username=Name  , password=password)
        print(Name,password)
        print(user)
        if user is None:
            return redirect(homepage)
             # A backend authenticated the credentials
        else:
            return render(request,'login.html')
        #      # No backend authenticated the credentials
    return render(request,'login.html')

def logoutuser(request):
    logout(request) 
    return redirect('/login')

def mobiles(request):
    return render(request,'mobiles.html')
    # return HttpResponse("this is about page")

def laptop(request):
    pro = Product.objects.all()
    print(pro)
    display = {'info':pro}

    return render(request,'laptop.html',display)

def viewdata(request):
    login_de = Login.objects.all()
    print(login_de)
    new = {'data':login_de}
    return render(request,'temp.html',new)

    