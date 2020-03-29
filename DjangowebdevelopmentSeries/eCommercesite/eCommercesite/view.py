from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    
    return render(request,"home_page.html",{})

def cart_page(request):
    
    return render(request,"cart_page.html",{})
def login_page(request):
    
    return render(request,"login_page.html",{})

def signup_page(request):
    
    return render(request,"signup_page.html",{})

def contact_page(request):
    return render(request,"contact_page.html",{})