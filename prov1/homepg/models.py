from django.db import models
from django.urls import reverse
from django.contrib import admin

# Create your models here.
# 用攤販當例子

class Vendor(models.Model):
    vendor_name=models.CharField(max_length=20)
    store_name=models.CharField(max_length=10)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

    #override
    def __str__(self):
        return self.vendor_name
    def get_absolute_url(self):
        return reverse("vendors:vendor_id",kwargs={"a":self.id})

class product(models.Model):
    product_name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=3,decimal_places=0)
    product_vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Vendor._meta.fields]
    list_filter=('phone',)
