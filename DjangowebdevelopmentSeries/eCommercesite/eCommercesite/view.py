from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    
    return render(request,"home_page.html",{})

def cart_page(request):
    
    return render(request,"cart_page.html",{})
