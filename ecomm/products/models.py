from django.db import models
from sellers import models as sellers

# Create your models here.

# category
class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoryName

# categoryid
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatgName = models.CharField(max_length=50,default="")
    crearedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subcatgName

# products
class Products(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    productImages = models.ImageField(upload_to="media/productimg",default="")

    def __str__(self):
        return self.title
        
# product_details
class ProductDetails(models.Model):
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    smallDescription = models.CharField(max_length=150)
    seller = models.ForeignKey(sellers.Seller,on_delete=models.CASCADE)

    def __str__(self):
        return self.products

# product_review
class Review(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comments = models.CharField(max_length=250)
    postedOn = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.comments



