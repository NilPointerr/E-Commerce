from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact,Login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout

def homepage(request):
    # if request.User.is_anonymous:
    #     return redirect('/login')
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
def login(request):
    if request.method =='POST':
        Name = request.POST['Name']
        # print(Name)
        password = request.POST['password']
        # print(password)
        login =Login(Name = Name, password = password)
        # print(Login(Name = Name, password = password))
    
        login.save()
        print('@#$%#@@@$$@@@@@@@@@@@@@@')
        messages.success(request, 'your login is succesfull')

        # user = authenticate(username=Email, password=password)
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        # if user is not None:
        #     print()
        #     return redirect('/index')
        #      # A backend authenticated the credentials
        # else:
        #     return render(request,'login.html')

        #      # No backend authenticated the credentials
    return render(request,'login.html')

def logout(request):
    logout(request) 
    return render(request,'login.html')

    