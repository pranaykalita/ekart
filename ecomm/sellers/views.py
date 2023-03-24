from django.shortcuts import render, redirect
from products.models import Category, SubCategory, Products


def dashboard(request):
    return render(request, 'sales/dashboard.html')


def product(request):
    return render(request, 'sales/products.html')


def category(request):
    categorylist = Category.objects.all()
    subcategorylist = SubCategory.objects.select_related('category').all()
    context = {
        'categorylist': categorylist,
        'subcategorylist': subcategorylist,
    }
    return render(request, 'sales/category.html', context)


def addCategory(request):
    if request.method == "POST":
        categoryName = request.POST.get("addcategoryField")
        savecatg = Category(categoryName=categoryName)
        savecatg.save()
        return redirect('/sales/category/')

    return render(request, 'sales/category.html')


def addSubCategory(request):
    if request.method == "POST":
        categoryNameId = request.POST.get("category_name")
        SubcategoryName = request.POST.get("subcategory")

        saveSubcatg = SubCategory(subcatgName=SubcategoryName,category_id=categoryNameId)
        saveSubcatg.save()
        return redirect('/sales/category/')

    return render(request, 'sales/category.html')


def deleteCategory(request):
    if request.method == "POST":
        categoryId = request.POST.get("category_name")

        delcatg = Category.objects.get(id=categoryId)
        delcatg.delete()
        return redirect('/sales/category/')
    return render(request, 'sales/category.html')

def deleteSubCategory(request):
    if request.method == "POST":
        subcategoryID = request.POST.get("subcategoryid")
        delsubcatg = SubCategory.objects.get(id=subcategoryID)
        delsubcatg.delete()
        return redirect('/sales/category/')
    return render(request, 'sales/category.html')


def Products(request):
    productList = Products.objects.all()
    context = {
        'prouductList': productList,
    }
    return render(request, 'sales/products.html', context)
