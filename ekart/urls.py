from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('admin/', admin.site.urls),

    # frontend

    path('', include('frontend.urls')),

    # cart from order
    path('cart/', include('cart.urls')),

    # api
    path('api/', include('api.urls')),

    # seller Dashbaord
    path('seller/', include('sellers.urls')),

    # accounts
    path('accounts/', include('accounts.urls')),


]

# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
