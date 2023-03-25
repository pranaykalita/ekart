from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request ,'seller/static/sellerlogin.html')

def home(request):
    return render(request ,'seller/static/dashboard.html')

def products(request):
    return render(request ,'seller/static/products.html')