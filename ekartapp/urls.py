
from django.contrib import admin
from django.urls import path

# import apps
from apphome import views as homeapp
from accounts import views as accountapp

urlpatterns = [
    path('admin/', admin.site.urls),

    #appHome
    path('', homeapp.mainrender, name='home'),

    # account pages
    path('account', accountapp.account , name='accountpage'),
    path('account/login/', accountapp.login , name='loginpage'),
    path('account/register', accountapp.register , name='registerpage'),
    path('logout', accountapp.logout , name='logout'),
]
