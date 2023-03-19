from django.db import models

# Create your models here.

class ek_category(models.Model):
    id = models.IntegerField(primary_key=True)
    catg_name = models.CharField(max_length = 150)
    createdon = models.DateTimeField(auto_now=False, auto_now_add=False)

class ek_subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    catg_id = models.ForeignKey(ek_category, on_delete=models.CASCADE)
    subcatg_name = models.CharField(max_length = 150)
    createdon = models.DateTimeField(auto_now=False, auto_now_add=False)

class ek_products(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 150)
    price = models.FloatField()
    qty = models.IntegerField()
    # seller FK
    catg_id = models.ForeignKey(ek_category, on_delete=models.CASCADE)
    subcatg_id = models.ForeignKey(ek_subcategory, on_delete=models.CASCADE)
    prod_image = models.URLField(max_length = 200)
    
    
class ek_products_details(models.Model):
    id = models.IntegerField(primary_key=True)
    prod_id = models.ForeignKey(ek_products, on_delete=models.CASCADE)
    prod_description = models.CharField(max_length = 1500)
    prod_smalldescription = models.CharField(max_length = 150)
    
class ek_products_images(models.Model):
    prod_id = models.ForeignKey(ek_products, on_delete=models.CASCADE)
    prod_images = models.ImageField(upload_to='product_images')
    

