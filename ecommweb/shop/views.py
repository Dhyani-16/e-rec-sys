from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shopHome(request):
    return render(request,'Home.html')

def cart(request):
    return render(request,'cart.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def productPreview(request):
    return render(request,'productPreview.html')
