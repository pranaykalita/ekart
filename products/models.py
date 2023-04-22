from django.db import models
from PIL import Image
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')
    subcatgName = models.CharField(max_length=50,default="")
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subcatgName

# products
class Product(models.Model):
    item = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='productcategories')
    subCategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='productsubcategories')

    image = models.ImageField(upload_to='media/productimg')

    # resize the image to set size on script
    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self
        width, height = img.size

        if img.height > 500 or img.width > 500:
            ratio = min(500 / width, 500 / height)
        elif img.height < 500 or img.width < 500:
            ratio = 1

        new_width = round(width * ratio)
        new_height = round(height * ratio)

        # resize the image
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # create a new image with the target size, centered on a black background
        background = Image.new('RGBA', (500, 500), (0, 0, 0, 255))
        x = (500 - new_width) // 2
        y = (500 - new_height) // 2
        background.paste(img, (x, y))

        img.save(self.image.path)

    def __str__(self):
        return self.item

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,related_name='product')
    about = models.TextField()
    SKU = models.CharField(max_length=100,default="")
    description = models.TextField()

    def __str__(self):
        return f"{self.product.item} details"





