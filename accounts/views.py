from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from .models import *


# Customer Login Register
def loginRegisterView(request):
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
                lastname =lastname,
                email=email,
                password=password,
                username=username
            )
            # account.save()
            return redirect('frontendhome')

    #     login ACCOUNT
    if 'login' in request.POST:
        if request.method == "POST":
            email = request.POST['user-email']
            password = request.POST['user-password']
            customer = authenticate(request, email=email,password=password)

            if customer is not None and customer.is_customer and customer.is_staff == False:
                login(request,customer)
                return redirect('frontendhome')
            else:
                return redirect('frontendlogin')

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
            return redirect('registerseller')

        seller  = customerUser.objects.create_seller(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            username=username,
            is_seller = True
        )
        # seller.save()
        # sellerid = seller.id
        # seller_name = customerUser.objects.get(pk=sellerid)

        gender = request.POST.get('gender')
        ccode = request.POST.get('ccode')
        phone = request.POST.get('phone')
        profileIMG = request.FILES.get('profileImg')

        seller.customer.create(
            gender = gender,
            countrycode = ccode,
            mobileno = phone,
            profileimg = profileIMG,
        )
        # seller_data.save()
        return redirect('sellerlogin')

    return render(request,'seller/pages/sellerRegister.html')

# seller Login
def sellerlogin(request):
    if request.user.is_authenticated:
        return redirect('/seller/dashboard')
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            seller = authenticate(request, email=email, password=password)

            print(email,password)
            if seller is not None and seller.is_seller and seller.is_staff == True:
                print('insdide if not none')
                login(request, seller)
                return redirect('/seller/dashboard')

            else:
                print('returning else part')
                return render(request, 'seller/pages/sellerlogin.html')
        return render(request, 'seller/pages/sellerlogin.html')

# selelr Logout
def sellerlogout(request):
    logout(request)
    return redirect('/seller/login')
