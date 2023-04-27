from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rentaiha.models import Iha
from django.contrib.auth import authenticate, login
from rentaiha.forms import IhaForm
from django.contrib.auth.models import User
from django.db.models import Q



def search_iha(request):
    return render(request, 'index.html')

def add_iha(request):
    return render(request, 'home.html')

def admin_iha(request):
    return render(request, 'myadmin.html')

def update_iha(request,id):
    
    return render(request, 'update.html',context={'id':id})


#Giriş Ekranı
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('myadmin')
        else:
            return HttpResponse("şifre kullanıcı adı yanlış")

    return render(request, 'login.html')

#Kayıt Ol Ekranı
def SignupPage(request):
    if request.method=='POST':
        f_name=request.POST.get('f_name')
        s_name=request.POST.get('s_name')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user = User.objects.create_user(username=uname, email=email,password=password)
        user.is_active = False
        user.first_name = f_name
        user.last_name = s_name
        user.save()
        print(uname,email,password)
        return HttpResponse("Cretae")
    return render(request , 'register.html')

