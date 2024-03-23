from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        baddress = request.POST.get('baddress')
        password = request.POST.get('password')
        password2 = request.POST.get('passwod2')
        # if password != password2:
        #     raise ValidationError('password not match')
        user = User.objects.create(username=username, email=email,first_name=fname,last_name=lname,password=password)
        Account.objects.create(user=user,phone=phone,address=address,billing_address=baddress)
        return redirect('account:login')
    else:
        return render(request, 'accounts/register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.error(request,'Invalid username or password')
        if user:
            return redirect('home:home')
    else:
        return render(request, 'accounts/login.html')