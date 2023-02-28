from django.contrib import admin
from .models import accountData

# Register your models here.
@admin.register(accountData)
class accountclass(admin.ModelAdmin):
    list_display=['id','userid','userphone','country','city']
