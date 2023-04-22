from django.urls import path
from .views import *

urlpatterns = [

    # login-SELLER
    path('login/', sellerlogin, name="sellerlogin"),
    path('logout/', sellerlogout, name="sellerlogout"),

    #     SIGNUP-seller
    path('createaccount/',sellerRegister,name="registerseller"),

]
