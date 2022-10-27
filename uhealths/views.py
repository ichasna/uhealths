import datetime, json
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from uhealths.models import UserProfile, UserProfileManger
from uhealths.forms import UserProfileCreationForm

@login_required(login_url='/uhealths/login/')
def landingpage(request):
    return render(request, 'landingpage.html')

def register(request):
    #form = UserCreationForm()
    form  = UserProfileCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
       
        #user = UserProfile()
        #user.objects.create_user()
        #user_login = authenticate()
        
        
        #if form.is_valid():
            #form.save()

            
            
            #messages.success(request, 'Akun berhasil dibuat!')
            return redirect('uhealths:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("uhealths:landingpage"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('uhealths:login'))
    response.delete_cookie('last_login')
    return response