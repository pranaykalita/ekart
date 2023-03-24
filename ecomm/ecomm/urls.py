
from django.contrib import admin
from django.urls import path


from sellers import views as salesapp

urlpatterns = [
    path('admin/', admin.site.urls),


    # sales Dashbaord
    path('sales/', salesapp.dashboard , name="dashboard"),
    path('sales/dashboard/', salesapp.dashboard , name="dashboard"),

    path('sales/category/', salesapp.category , name="category"),

    path('sales/addcategory/', salesapp.addCategory, name="addcategory"),
    path('sales/deletecategory/', salesapp.deleteCategory, name="deletecategory"),
    path('sales/addsubcategory/', salesapp.addSubCategory, name="addsubcategory"),
    path('sales/deletesubcategory/', salesapp.deleteSubCategory, name="deletesubcategory"),

    path('sales/products/', salesapp.product , name="products"),


]
