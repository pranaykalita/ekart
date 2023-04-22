from django.urls import path
from .views import *
from accounts.views import *

urlpatterns = [

    path('', homepageView,name="frontendhome"),
    path('product/item/<str:id>/', singleproductView),

    path('login/', loginRegisterView),





]
