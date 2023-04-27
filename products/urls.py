from django.urls import path
from .views import *

urlpatterns = [

    path('', addocart,name="addtocart"),

]
