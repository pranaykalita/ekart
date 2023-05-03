from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from accounts.models import customerUser
from products.models import Category, SubCategory, Product, ProductDetail, ProductImage


# SELLER ID SESSION
def sellersession(request):
    seller_id = request.session.get('seller_id')
    seller = customerUser.objects.get(id=seller_id)
    return seller


# dashboard
@login_required(login_url='sellerlogin')
def dashboard(request):
    productcount = Product.objects.count()
    catCount = Category.objects.count()
    subcatCount = SubCategory.objects.count()
    context = {'prodCount': productcount,
               'catCount': catCount,
               'subCatCount': subcatCount,
               }
    return render(request, 'seller/pages/dashboard.html', context)


# category
@login_required(login_url='sellerlogin')
def category(request):
    categorylist = Category.objects.all()
    subcategorylist = SubCategory.objects.select_related('category').all()
    context = {
        'categorylist': categorylist,
        'subcategorylist': subcategorylist,
    }
    return render(request, 'seller/pages/category.html', context)


# products
@login_required(login_url='sellerlogin')
def product(request):
    seller = sellersession(request)
    categories = Category.objects.all()
    subcategories = SubCategory.objects.select_related('category').all()

    product = Product.objects.filter(seller=seller).select_related('product')
    context = {'categories': categories,
               'subcategories': subcategories,
               'productList': product,
               'segment': 'SellerProduct',
               }
    return render(request, 'seller/pages/products.html', context)


# orders
@login_required(login_url='sellerlogin')
def orders(request):
    return render(request, 'seller/pages/orders.html')


# invoices
@login_required(login_url='sellerlogin')
def invoice(request):
    return render(request, 'seller/pages/invoices.html')


# messages
@login_required(login_url='sellerlogin')
def Messages(request):
    return render(request, 'seller/pages/messages.html')


# addCategory
@login_required(login_url='sellerlogin')
def addCategory(request):
    if request.method == "POST":
        categoryName = request.POST.get("addcategoryField")
        savecatg = Category(categoryName=categoryName)
        savecatg.save()
        return redirect('sellercategory')
    return render(request, 'seller/pages/category.html')


# Update Category
@login_required(login_url='sellerlogin')
def updateCategory(request, id):
    if request.method == "POST":
        catgdetails = Category.objects.get(id=id)
        categoryname = request.POST.get("updatecategory")
        catgdetails.categoryName = categoryname
        catgdetails.updatedOn = timezone.now()
        catgdetails.save()
        return redirect('sellercategory')
    return render(request, 'seller/pages/categoty.html')


# Delete Category
@login_required(login_url='sellerlogin')
def deleteCategory(request):
    if request.method == "POST":
        categoryId = request.POST.get("category_name")
        delcatg = Category.objects.get(id=categoryId)
        delcatg.delete()
        return redirect('sellercategory')
    return render(request, 'seller/pages/category.html')


# Add Sub Category
@login_required(login_url='sellerlogin')
def addSubCategory(request):
    if request.method == "POST":
        categoryNameId = request.POST.get("category_name")
        SubcategoryName = request.POST.get("subcategory")
        saveSubcatg = SubCategory(subcatgName=SubcategoryName, category_id=categoryNameId)
        saveSubcatg.save()
        return redirect('sellercategory')
    return render(request, 'seller/pages/category.html')


# Delete Sub Category
@login_required(login_url='sellerlogin')
def deleteSubCategory(request):
    if request.method == "POST":
        subcategoryID = request.POST.get("subcategoryid")
        delsubcatg = SubCategory.objects.get(id=subcategoryID)
        delsubcatg.delete()
        return redirect('sellercategory')
    return render(request, 'seller/pages/category.html')


# Update Sub Category
@login_required(login_url='sellerlogin')
def updatesubCategory(request, id):
    if request.method == "POST":
        subcatgdetails = SubCategory.objects.get(id=id)
        newname = request.POST.get("subcategoryname")
        subcatgdetails.subcatgName = newname
        subcatgdetails.updatedOn = timezone.now()
        subcatgdetails.save()
        return redirect('sellercategory')
    return render(request, 'seller/pages/categoty.html')


# Add Products
@login_required(login_url='sellerlogin')
def Addproduct(request):
    if request.method == "POST":

        itemname = request.POST.get("itemname")
        itemprice = request.POST.get("itemprice")
        itemqty = request.POST.get("itemqty")
        itemcategoryID = request.POST.get("itemcategory")
        category = Category.objects.get(pk=itemcategoryID)
        itemsubCategoryID = request.POST.get("itemsubcategory")
        subcategory = SubCategory.objects.get(pk=itemsubCategoryID)

        itemimg = request.FILES.get("itemimg")

        itemimg1 = request.FILES.get("itemimg1")
        itemimg2 = request.FILES.get("itemimg2")
        itemimg3 = request.FILES.get("itemimg3")

        # seller
        seller_id = request.session.get('seller_id')
        seller = customerUser.objects.get(id=seller_id)

        # productDetails
        itemAbout = request.POST.get("itemabout")
        itemDesc = request.POST.get("itemdescription")
        sku = request.POST.get("sku")

        prodMain = Product(item=itemname, price=itemprice, quantity=itemqty, category=category, subCategory=subcategory,
                           seller=seller, image=itemimg)

        prodMain.save()

        prod_id = prodMain.id
        product = Product.objects.get(pk=prod_id)

        prod = ProductDetail(product=product, about=itemAbout, SKU=sku, description=itemDesc)
        prod.save()

        if itemimg or itemimg1 or itemimg2 or itemimg3:
            if itemimg:
                prodimg1 = ProductImage(product=product, image=itemimg)
                prodimg1.save()

            if itemimg1:
                prodimg1 = ProductImage(product=product, image=itemimg1)
                prodimg1.save()

            if itemimg2:
                prodimg2 = ProductImage(product=product, image=itemimg2)
                prodimg2.save()

            if itemimg3:
                prodimg3 = ProductImage(product=product, image=itemimg3)
                prodimg3.save()

        return redirect('sellerproducts')


# Delete Products
@login_required(login_url='sellerlogin')
def deleteproduct(request, id):
    if request.method == "POST":
        delprod = Product.objects.get(id=id)
        delprod.delete()
        return redirect('sellerproducts')
    return render(request, 'seller/pages/products.html')


# Update Products
@login_required(login_url='sellerlogin')
def updateproduct(request, id):
    if request.method == "POST":
        name = request.POST.get("itemname")
        price = request.POST.get("itemprice")
        quantity = request.POST.get("itemqty")
        category = request.POST.get("itemcategory")
        categoryID = Category.objects.get(pk=category)
        subcategory = request.POST.get("itemsubcategory")
        subcategoryID = SubCategory.objects.get(pk=subcategory)
        about = request.POST.get("itemabout")
        description = request.POST.get("itemdescription")

        image = request.FILES.get("itemimg")

        productSelect = Product.objects.get(id=id)
        subProduct = ProductDetail.objects.get(product=id)

        # if notselected take name from item
        if image:
            # if new update
            productSelect.image = image
            productSelect.save()
        else:
            pass
        productSelect.item = name
        productSelect.price = price
        productSelect.quantity = quantity
        productSelect.category = categoryID
        productSelect.subCategory = subcategoryID
        productSelect.save()
        subProduct.about = about
        subProduct.description = description
        subProduct.save()
        return redirect('sellerproducts')

    return render(request, 'seller/pages/products_content.html')
