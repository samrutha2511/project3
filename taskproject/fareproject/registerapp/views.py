from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login')


    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')

            else:
                user=User.objects.create_user(username=uname, email=email,first_name=fname,last_name=lname,password=password)

                user.save()
                return redirect('login')
                print('User Created')

        else:
            messages.info(request, 'Password incorrect')
            return redirect('register')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')