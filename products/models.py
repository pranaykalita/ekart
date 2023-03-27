from django.db import models
from django.utils import timezone
from sellers import models as sellers

# Create your models here.

# category
class Category(models.Model):
    categoryName = models.CharField(max_length=20)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoryName

# categoryid
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcatgName = models.CharField(max_length=50,default="")
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcatgName

# products
class Product(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/productimg')

    def __str__(self):
        return self.item

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    about = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.product.item} details"





