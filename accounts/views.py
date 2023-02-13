from django.shortcuts import render,redirect
from django.contrib import messages

# usermodel builtin
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        firstname = request.POST.get("FirstName")
        lastname = request.POST.get("LastName")
        email = request.POST.get("email")
        passwordcnf = request.POST.get("cnfpassword")

        user = User.objects.create_user(username=username,
                                        first_name=firstname,
                                        last_name=lastname,
                                        email=email,
                                        password=passwordcnf)
        user.save
        return render(request, 'account/login.html')
    return render(request, 'account/register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/account')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'account/account.html')
        else:
            return redirect('/')
    else:
        return render( request, 'account/login.html')

   

def logout(request):
    auth.logout(request)
    return render(request,'mainapp/home.html')


# add decorator
@login_required(login_url='account/login')
def account(request):
    return render(request, 'account/account.html')
