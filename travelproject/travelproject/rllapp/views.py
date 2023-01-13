from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")



def register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['secondname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['password']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username Taken")
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('register.html')
            else:
                 user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
                 user.save();
                 return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')