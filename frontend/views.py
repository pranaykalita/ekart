from django.shortcuts import render
import requests
from django.conf import settings
from accounts.models import *


# Lsit all Product
def homepageView(request):
    # fetch category And SubCategory
    category_response = requests.get('http://127.0.0.1:8000/api2/categorylist/')
    category = category_response.json()

    # fetch product
    product_response = requests.get('http://127.0.0.1:8000/api2/products/')
    products = product_response.json()
    context = {'categories': category,
               'products': products}
    return render(request, 'Frontend/pages/home.html', context)


# single Product
def singleproductView(request, id):
    url = 'http://127.0.0.1:8000/api2/product/item/' + id
    producturl = requests.get(url)
    products = producturl.json()
    context = {'product': products}
    print(context)
    return render(request, 'Frontend/pages/singleprod.html', context)


def prdouctView(request):
    return render(request, 'Frontend/pages/singleprod.html')


def testv(request):
    category = request.GET.get('cat')
    cat = requests.get('http://127.0.0.1:8000/api2/categorylist/')
    categorylist = cat.json()
    if category:
        url = f'http://127.0.0.1:8000/api2/product/item/?cat={category}'
    else:
        url = 'http://127.0.0.1:8000/api2/product/item/'

    response = requests.get(url)
    products = response.json()

    return render(request, 'Frontend/pages/test.html',{'products': products,'categorylist': categorylist,})
