from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact,Login
from django.contrib import messages

def homepage(request):
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
        Email = request.POST['Email']
        password = request.POST['password']
        login =Login(Email = Email, password = password)
        login.save()
        messages.success(request, 'your login is succesfull')

    return render(request,'login.html')


    