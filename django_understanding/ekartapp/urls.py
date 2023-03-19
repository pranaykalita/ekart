
from django.contrib import admin
from django.urls import path

# import apps
from seller import views as saleapp

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', accountapp.login ,name='home'),

    # account pages
    path('sales', saleapp.saleshome , name='dashboard'),
   
]
