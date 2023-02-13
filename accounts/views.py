from django.shortcuts import render,redirect
from django.contrib import messages

# usermodel builtin
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request,'mainapp/home.html')

def login(request):
    if User.is_authenticated :
        print("if part loggedin")
        print(User.is_authenticated)
    else:
        print("else not login")
        print(User.is_authenticated)
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'account/account.html')
            else:
                return redirect('/')
    return render(request, 'account/login.html')


def register(request):

    # get registration form post requests

    if request.method == "POST":

        username = request.POST.get("Username")
        firstname = request.POST.get("FirstName")
        lastname = request.POST.get("LastName")
        email = request.POST.get("email")
        passwordcnf = request.POST.get("cnfpassword")

        # save to database
        user = User.objects.create_user(username=username,password=passwordcnf,email=email,first_name=firstname,last_name=lastname)
        user.save
        return redirect('account/login.html')

    return render(request, 'account/register.html')

# add decorator
@login_required(login_url='account/login')
def account(request):
    return render(request, 'account/account.html')
