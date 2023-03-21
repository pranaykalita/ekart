
from django.contrib import admin
from django.urls import path

from sellers import views as sales
from accounts import views as accounts

urlpatterns = [
    path('admin/', admin.site.urls),

    # sales
    path('sales', sales.dashboard ,name="dashboard"),
    path('sales/login', accounts.sellerlogin , name="salelogin"),
    path('sales/logout', accounts.sellerlogout , name="logout"),

    path('sales/dashboard', sales.dashboard , name="dashboard"),
    path('sales/products', sales.product , name="products"),
]
