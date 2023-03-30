from django.shortcuts import render, redirect
from products.models import *
def home(request):
    return render(request, 'home.html')