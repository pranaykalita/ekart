from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'products', ProductListView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # seller Dashbaord
    path('seller/', include('sellers.urls')),

]

# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
