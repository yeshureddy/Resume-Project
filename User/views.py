from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
#from djnago.http import redirect
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Account already exists,try logging in')
            return redirect('register')
        else:
            if password==password2:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('user/')
            else:
                messages.info(request,'Passwords not matching')
                return redirect('register')
        return redirect('/')    
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uid']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/user')
        else:
            messages.info(request,'Wrong Username or Password')
        
            return redirect('signin')

    else:
       return render(request,'signin.html') 

def logout(request):
    auth.logout(request)
    return redirect('')