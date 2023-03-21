from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/sales/login')
def dashboard(request):
    return render(request , 'sales/dashboard.html')

@login_required(login_url='/sales/login')
def product(request):
    return render(request , 'sales/products.html')