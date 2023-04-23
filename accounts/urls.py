from django.urls import path
from .views import *

urlpatterns = [

    # Global Logout
    path('logout/', logoutSession, name="globallogout"),

    # login-SELLER
    path('seller/login/', sellerlogin, name="sellerlogin"),
    # login Customer
    path('customer/login/', loginRegisterView, name="customerlogin"),

    # Register seller
    path('seller/createaccount/', sellerRegister, name="sellerregister"),
    # Register Customer
    path('customer/createaccount/', loginRegisterView, name="customerRegister")

]
