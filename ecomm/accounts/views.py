from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
# Create your views here.


# def sellerlogin(request):
#     if request.user.is_authenticated:
#         return render( request, 'sales/dashboard.html')
#     elif request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             return render(request, 'sales/dashboard.html')
#             # return redirect('/sales/dashboard')
#         else:
#             # messages.warning(request, 'Invalid Credintials')
#             return render( request, 'sales/sellerlogin.html')
#     else:
#         return render( request, 'sales/sellerlogin.html')

