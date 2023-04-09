from django.shortcuts import render

# Create your views here.
def homepage(request):
    return  render(request, 'Frontend/home-page.html')

def product(request):
    return  render(request, 'Frontend/product-page.html')