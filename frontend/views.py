from django.shortcuts import render
import requests


# Create your views here.

def homepage(request):
    # fetch category
    category_response = requests.get('http://localhost:8000/api/category/')
    category = category_response.json()

    # fetch product
    product_response = requests.get('http://127.0.0.1:8000/api/products')
    products = product_response.json()
    context = {'category': category,
               'products': products}

    # return render(request, 'Frontend/Backup_/home-page.html',context)
    return render(request, 'Frontend/pages/home.html', context)


def singleproduct(request, id):
    url = 'http://127.0.0.1:8000/api/products/' + id
    producturl = requests.get(url)
    products = producturl.json()
    context = {'product': products}
    print(context)
    return render(request, 'Frontend/pages/singleprod.html', context)

def testpage(request):
    return render(request,'Frontend/pages/singleprod.html')