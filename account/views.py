from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.


def home(request):
    return render(request, 'account/home.html') 


def register(request):
     if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # print('password-->',password1)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email taken')
                 return redirect('register')
            else:        
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request, 'account/login.html')
        else:
            messages.info(request,'Password not match')
            return render(request, 'account/register.html')                        
            # print('Password not match')    

     else:
        return render(request, 'account/register.html')    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/todo/index/' + username)            
        else:
             return redirect('login')
        

    else:
         return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')