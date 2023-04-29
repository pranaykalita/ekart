from django.shortcuts import render
import requests
import json
from products.models import Category,Product
from django.conf import settings
from accounts.models import *

def get_categories():
    response = requests.get('http://127.0.0.1:8000/api/categorylist/')
    if response.status_code == 200:
        data = json.loads(response.content)
        return data
    else:
        return []

# Lsit all Product
def homepageView(request):

    # fetch category And SubCategory
    category_response = requests.get('http://127.0.0.1:8000/api/categorylist/')
    category = category_response.json()

    # fetch product
    product_response = requests.get('http://127.0.0.1:8000/api/products/')
    products = product_response.json()
    context = {'categories': category,
               'products': products}
    return render(request, 'Frontend/pages/home.html', context)


# single Product
def singleproductView(request, id):
    category = get_categories()
    url = 'http://127.0.0.1:8000/api/product/item/' + id
    producturl = requests.get(url)
    products = producturl.json()
    customer = request.session.get('customer_id')
    print(customer)
    context = {'product': products, 'categories': category, 'customer_id':customer}

    return render(request, 'Frontend/pages/singleprod.html', context)


# product
def productsView(request):
    category = get_categories()

    selected_category = request.GET.get('cat', None)

    print(selected_category)
    if selected_category:
        product_response = requests.get(f'http://127.0.0.1:8000/api/products/?cat={selected_category}')
    else:
        product_response = requests.get('http://127.0.0.1:8000/api/products/')

    products = product_response.json()


    context = {'products': products,
               'categories': category,
               }
    return render(request, 'Frontend/pages/products.html',context)