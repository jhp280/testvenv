from django.contrib import admin
from django.urls import path

from .import views

app_name='vendors'
urlpatterns = [
    path('', views.showtemplate),
    path('test<int:a>/',views.unitrecord,name='vendor_id'),
    path('add',views.vendor_add_views)
]
