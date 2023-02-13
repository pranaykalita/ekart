from django.shortcuts import render

# Create your views here.

#homepage

def mainrender(request):
    return render(request,'mainapp/home.html')