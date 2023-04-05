from django.shortcuts import render

# Create your views here.
def homepage(request):
    return  render(request, 'frontend/pages/home.html')

def product(request):
    return  render(request, 'frontend/pages/product.html')