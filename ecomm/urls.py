from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),

    # seller Dashbaord
    path('seller/', include('sellers.urls'))


]
