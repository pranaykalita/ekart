from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
# Create your views here.


# seller register
def sellerRegister(request):
    return render(request,'seller/pages/sellerRegister.html')
# seller Login
def sellerlogin(request):
    if request.user.is_authenticated:
        return redirect('/seller/dashboard')
    else:
        # return redirect('/')
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/seller/dashboard')
            else:
                return render(request, 'seller/pages/sellerlogin.html')
        return render(request, 'seller/pages/sellerlogin.html')
def sellerlogout(request):
    auth.logout(request)
    return redirect('/seller/login')
