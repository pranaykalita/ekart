from django.urls import path
from .views import *

urlpatterns = [

    # login-SELLER
    path('login/', sellerlogin, name="login"),
    path('logout/', sellerlogout, name="sellerlogout"),
    #     SIGNUP-seller
    path('registeraccount/',sellerRegister,name="registerseller"),

]
