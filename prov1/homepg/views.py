from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

# -*- coding: utf-8 -*-

def homepg(request):
    return HttpResponse("中文測試")

def math(request,a,b):
    s=int(a)+int(b)
    d=int(a)-int(b)
    p=int(a)*int(b)
    q=int(a)/int(b)
    html='<html>sum={s}<br>dif={d}<br>pro={p}<br>quo={q}</html>'.format(s=s,d=d,p=p,q=q)
    return HttpResponse(html)
