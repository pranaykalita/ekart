from django.db import models
from sellers import models as sellers

# Create your models here.

# category
class ecom_category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    catg_name = models.CharField(max_length=20)
    createdon = models.DateTimeField()

    def __str__(self):
        return self.catg_name

# categoryid
class ecom_subcategory(models.Model):
    category_id = models.ForeignKey(ecom_category, on_delete=models.CASCADE)
    subcatg_name = models.CharField(max_length=50,default="")
    crearedon = models.DateTimeField()

    def __str__(self):
        return self.subcatg_name

# products
class ecom_products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    category_id = models.ForeignKey(ecom_category, on_delete=models.CASCADE,default="")
    subcategory_id = models.ForeignKey(ecom_subcategory, on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to="media/productimg",default="")

    def __str__(self):
        return self.title
        
# product_details
class ecom_productDetails(models.Model):
    product_id = models.ForeignKey(ecom_products,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    small_description = models.CharField(max_length=150)
    seller_id = models.ForeignKey(sellers.ecom_seller,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id

# product_review
class ecom_review(models.Model):
    product_id = models.ForeignKey(ecom_products, on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comments = models.CharField(max_length=250)
    postedon = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.comments



