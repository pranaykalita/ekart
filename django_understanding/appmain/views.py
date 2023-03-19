from django.shortcuts import render

# Create your views here.
def saleshome(request):
    return render(request, 'seller_dash/index.html')