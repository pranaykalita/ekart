import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from orders.models import *


# cart Items in cartPage
@login_required(login_url='customerlogin')
def cartpage(request):
    userid = request.session.get('customer_id')
    # create cart if not present
    created = Cart.objects.get_or_create(customeruser=request.user)

    cartuuid = Cart.objects.filter(customeruser=userid).first()

    url = f"http://127.0.0.1:8000/api/cart/{userid}/{cartuuid}"

    cart_response = requests.get(url)
    cart_items = cart_response.json()

    context = {'cart_items': cart_items}

    return render(request, 'Frontend/pages/cart.html', context)


# Add to Cart
def addtocart(request, prod_id):
    userid = request.session.get('customer_id')
    cartuuid = Cart.objects.filter(customeruser=userid).first()

    if request.method == 'POST':
        prodid = prod_id
        product = Product.objects.get(id=prodid)
        prodQty = int(request.POST.get('qtybutton', 1))

        cart_item = CartItem.objects.filter(cart=cartuuid, product=product).first()
        # check already added
        if cart_item:
            cart_item.quantity += prodQty
            cart_item.save()
        else:
            CartItem(cart=cartuuid, product=product, quantity=prodQty).save()
        return redirect('cartpage')
    return redirect('cartpage')


# Clear the cart
def deltecart(request):
    userid = request.session.get('customer_id')
    cartuuid = Cart.objects.filter(customeruser=userid).first()
    cartuuid.delete()
    return redirect('frontendhome')


# clear item from cart
def deletecartItem(request, item_id):
    itemid = item_id
    CartItem.objects.filter(product=itemid).delete()
    return redirect('cartpage')


# count the cart
@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_cart_count(request):
    userid = request.session.get('customer_id')
    cartuuid = Cart.objects.filter(customeruser=userid).first()

    url = f"http://127.0.0.1:8000/api/cart/{userid}/{cartuuid}"

    cart_resp = requests.get(url)
    cart_itm = cart_resp.json()
    items = len(cart_itm.get('items', []))
    itemcount = "pranay"
    print(items)
    return Response({'itemcount': items}, template_name='Frontend/components/cart/counter.html')



# order_checkoutform
def order_process_payment(request):
    userid = request.session.get('customer_id')
    cartuuid = Cart.objects.filter(customeruser=userid).first()
    url = f"http://127.0.0.1:8000/api/cart/{userid}/{cartuuid}"
    cart_resp = requests.get(url)
    cart_itm = cart_resp.json()

    if request.method == 'POST':

        # get data
        country = request.POST.get('country')
        region = request.POST.get('region')
        zip = request.POST.get('zip')
        add1 = request.POST.get('address1')
        add2 = request.POST.get('address2')
        landmark = request.POST.get('landmark')
        phone = request.POST.get('phone')

        return render(request, 'Frontend/components/orders/checkout.html', )
    return render(request, 'Frontend/components/orders/checkout.html')