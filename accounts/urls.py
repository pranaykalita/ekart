from django.urls import path
from .views import *

urlpatterns = [

    # login
    path('login/',sellerlogin,name="login"),
    path('logout/',sellerlogout,name="sellerlogout"),

]
