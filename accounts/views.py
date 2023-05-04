from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import *


# Customer Login Register
def loginRegisterView(request):
    if request.user.is_authenticated:
        return redirect('frontendhome')
    else:
        # signup USER
        if 'signup' in request.POST:
            if request.method == "POST":
                username = request.POST['user-name']
                firstname = request.POST['user-firstname']
                lastname = request.POST['user-lastname']
                password = request.POST['user-password']
                email = request.POST['user-email']
                customerUser.objects.create_customer(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    password=password,
                    username=username
                )
                return redirect('frontendhome')

        # login ACCOUNT
        if 'login' in request.POST:
            if request.method == "POST":
                email = request.POST['user-email']
                password = request.POST['user-password']
                customer = authenticate(request, email=email, password=password)
                if customer is not None and customer.is_customer and customer.is_staff == False:
                    login(request, customer)
                    # store CUSTOMER ID
                    request.session['customer_id'] = customer.id
                    return redirect('frontendhome')
                else:
                    return redirect('customerlogin')
        return render(request, 'Frontend/pages/loginregister.html')


# seller register
def sellerRegister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if user already exists
        if customerUser.objects.filter(email=email).exists():
            print("exist alrady")
            return redirect('sellerregister')

        seller = customerUser.objects.create_seller(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            username=username,
            is_seller=True
        )
        gender = request.POST.get('gender')
        ccode = request.POST.get('ccode')
        phone = request.POST.get('phone')
        profiler = request.FILES.get("profileImg")

        seller.customer.create(
            gender=gender,
            countrycode=ccode,
            mobileno=phone,
            profileimg=profiler,
        )
        print(gender, phone, profiler )
        return redirect('sellerlogin')
    return render(request, 'seller/pages/sellerRegister.html')


# seller Login
def sellerlogin(request):
    if request.user.is_authenticated:
        return redirect('sellerdashboard')
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            seller = authenticate(request, email=email, password=password)
            if seller is not None and seller.is_seller and seller.is_staff == True:
                login(request, seller)
                # store SELLER ID
                request.session['seller_id'] = seller.id
                return redirect('sellerdashboard')
            else:
                return redirect('sellerlogin')
        return render(request, 'seller/pages/sellerlogin.html')


# Logout
def logoutSession(request):
    logout(request)
    # if request.path.startswith('/customer/'):
    #     return redirect('/home')
    # else:
    #     return redirect('/mvp')
    return redirect('frontendhome')
