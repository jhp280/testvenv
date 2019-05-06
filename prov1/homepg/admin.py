from django.contrib import admin

from .models import Vendor,product,VendorAdmin

# Register your models here.

#admin.site.register(Vendor,VendorAdmin)
admin.site.register(product)
