from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render, redirect

from cart.models import *


# Create your views here.

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
    if not cart_items:
        return render(request, 'Frontend/pages/cart.html')
    else:
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

        # if added already then inc prod quantity by update
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
