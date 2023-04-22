from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),

    # frontend

    path('', include('frontend.urls')),

    # api
    path('api/',include('api.urls')),
    path('api2/',include('api2.urls')),

    # seller Dashbaord
    path('seller/', include('sellers.urls')),
    path('seller/', include('accounts.urls')),

]

# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
