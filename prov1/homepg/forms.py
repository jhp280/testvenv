from django import forms

from .models import Vendor

class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'
        labels={'vendor_name': ('攤販名稱'),
                'store_name': ('店名'),
                'phone': ('電話'),
                'location': ('地址'),}

class RawVendorForm(forms.Form):
    vendor_name=forms.CharField()
    store_name=forms.CharField()
    phone=forms.CharField()
