from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Vendor
from .forms import VendorForm,RawVendorForm

# Create your views here.

# -*- coding: utf-8 -*-


def unitrecord(request,a):
    vendor_list=get_object_or_404(Vendor,id=a)
    '''try:
        vendor_list=Vendor.objects.get(id=a)
    except Vendor.DoesNotExist:
        raise Http404'''
    context={'vendor_list':vendor_list}
    return render(request,'homepgs/unittest.html',context)

def showtemplate(request):
    vendor_list=Vendor.objects.all()
    context={'vendor_list':vendor_list}
    return render(request,'homepgs/test.html',context)

def vendor_add_views(request):
    form=VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=VendorForm()
    context={"form":form}
    return render(request,'homepgs/vendor_add.html',context)
