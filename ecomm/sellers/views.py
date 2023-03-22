from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.



def dashboard(request):
    return render(request , 'sales/dashboard.html')


def product(request):
    return render(request , 'sales/products.html')

def category(request):
    return render(request , 'sales/category.html')

