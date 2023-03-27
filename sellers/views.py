from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from products.models import Category, SubCategory, Product, ProductDetail


def dashboard(request):
    return render(request, 'seller/dashboard.html')


def product(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.select_related('category').all()
    product = ProductDetail.objects.select_related('product').all()
    # products = Product.objects.all()
    # productdata = ProductDetail.objects.select_related('product').all()
    context = { 'categories' : categories,
                'subcategories' : subcategories,
                'product' : product,
                }
    return render(request, 'seller/products.html', context)


def category(request):
    categorylist = Category.objects.all()
    subcategorylist = SubCategory.objects.select_related('category').all()
    context = {
        'categorylist': categorylist,
        'subcategorylist': subcategorylist,
    }
    return render(request, 'seller/category.html', context)


def addCategory(request):
    if request.method == "POST":
        categoryName = request.POST.get("addcategoryField")
        savecatg = Category(categoryName=categoryName)
        savecatg.save()
        return redirect('/seller/category/')
    return render(request, 'seller/category.html')

def updateCategory(request,id):
    if request.method == "POST":
        catgdetails = Category.objects.get(id=id)
        categoryname = request.POST.get("updatecategory")
        catgdetails.categoryName=categoryname
        catgdetails.updatedOn=timezone.now()
        catgdetails.save()
        return redirect('/seller/category/')
    return render(request, 'seller/categoty.html')

def deleteCategory(request):
    if request.method == "POST":
        categoryId = request.POST.get("category_name")
        delcatg = Category.objects.get(id=categoryId)
        delcatg.delete()
        return redirect('/seller/category/')
    return render(request, 'seller/category.html')

def addSubCategory(request):
    if request.method == "POST":
        categoryNameId = request.POST.get("category_name")
        SubcategoryName = request.POST.get("subcategory")
        saveSubcatg = SubCategory(subcatgName=SubcategoryName,category_id=categoryNameId)
        saveSubcatg.save()
        return redirect('/seller/category/')
    return render(request, 'seller/category.html')

def deleteSubCategory(request):
    if request.method == "POST":
        subcategoryID = request.POST.get("subcategoryid")
        delsubcatg = SubCategory.objects.get(id=subcategoryID)
        delsubcatg.delete()
        return redirect('/seller/category/')
    return render(request, 'seller/category.html')

def updatesubCategory(request,id):
    if request.method == "POST":
        subcatgdetails = SubCategory.objects.get(id=id)
        newname = request.POST.get("subcategoryname")
        subcatgdetails.subcatgName = newname
        subcatgdetails.updatedOn = timezone.now()
        subcatgdetails.save()
        return redirect('/seller/category/')
    return render(request, 'seller/categoty.html')


def Addproduct(request):
    if request.method == "POST":
        itemname = request.POST.get("itemname")
        itemprice = request.POST.get("itemprice")
        itemqty = request.POST.get("itemqty")
        itemcategoryID = request.POST.get("itemcategory")
        itemsubCategoryID = request.POST.get("itemsubcategory")
        itemAbout = request.POST.get("itemabout")
        itemDesc = request.POST.get("itemdescription")
        itemimg = request.FILES.get("itemimg")

        return redirect('/seller/products/')
    return render(request, 'seller/products.html')

def deleteproduct(request,id):
        if request.method == "POST":
            delprod = Product.objects.get(id=id)
            delprod.delete()
            return redirect('/seller/products/')
        return render(request, 'seller/products.html')