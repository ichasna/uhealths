
import datetime, json
from distutils.command.clean import clean
import imp
import datetime, json, logging
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from uhealths.models import HealthStats
from uhealths.forms import HealthStatsForm

@login_required(login_url='/uhealths/login/')
def landingpage(request):
    return render(request, 'home.html')

#@login_required(login_url='/uhealths/login/')
def check_healths_status(request):
    form = HealthStatsForm()
    if(request.method == 'POST'):
        form = HealthStatsForm(request.POST)
        if form.is_valid:
            #form.instance.user = request.user

            
            data = HealthStats.objects.get(user = request.user)
            if data == None:
                form.instance.user = request.user
                form.save()
            else:
                clean_data = form.cleaned_data
                data.age = clean_data['age']
                data.height = clean_data['height']
                data.weight = clean_data['weight']
                data.gender = clean_data['gender']
                #form.save()
            bmr = 0
            if(data.gender == 'male'):
                bmr = 66.5 + (13.75*data.weight) + (5.003*data.height) -(6.75*data.age)
            else:
                bmr = 655.1 + (9,563 *data.weight) + (1.850 * data.height) - (4.676*data.age)
            bmi = data.weight/(data.height/100)**2
            HealthStats.objects.filter(user = request.user).update(bmr=bmr,bmi=bmi)
            
            return redirect()
    
    context = {'form':form}
    return render(request, 'check.html', context)


    



def register(request):
    form  = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
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
            response = HttpResponseRedirect(reverse("uhealths:menu"))
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

@login_required(login_url='/uhealths/login/')
def main_menu(request):
    return render(request, "menu.html")

def show_json(request):
   
    data = HealthStats.objects.filter(user = request.user)
    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def update_data(request):
    form = HealthStatsForm()
    if(request.method == 'POST'):
        form = HealthStatsForm(request.POST)
        if form.is_valid:
            #form.instance.user = request.user
            data = HealthStats.objects.get(user = request.user)
            if data == None:
                form.instance.user = request.user
                form.save()
            else:
                clean_data = form.cleaned_data
                data.age = clean_data['age']
                data.height = clean_data['height']
                data.weight = clean_data['weight']
                data.gender = clean_data['gender']
                #form.save()
            bmr = 0
            if(data.gender == 'male'):
                bmr = 66.5 + (13.75*data.weight) + (5.003*data.height) -(6.75*data.age)
            else:
                bmr = 655.1 + (9,563 *data.weight) + (1.850 * data.height) - (4.676*data.age)
            bmi = data.weight/(data.height/100)**2
            HealthStats.objects.filter(user = request.user).update(bmr=bmr,bmi=bmi)
            
            return HttpResponse()
    return HttpResponse()

def show_json(request):
    data = HealthStats.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


