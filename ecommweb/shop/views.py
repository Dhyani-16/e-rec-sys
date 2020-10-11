from django.shortcuts import render
from django.http import HttpResponse
from .models import Product_Detail,Order_detail,Rating_Detail,Product_Review,UsersQuery

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
    if request.method=="POST":
        
        product = Product_Detail.objects.filter(product_id=1)[0]
        print(product)
        if request.POST['formtype']=="rating":
            uname = request.POST['name']
            rating = request.POST['rating']
            product_id = request.POST['product_id']
            print(f"uname:{uname} , rating :{rating}, product_id : {product_id}")

            Rating_Detail.objects.create(
                rating_user_id = request.user,
                rating_product_id= product,
                rating = rating
            )
            
        elif request.POST['formtype']=='review':
            uname = request.POST['name']
            review = request.POST['review']
            product_id = request.POST['product_id']
            print(f"uname:{uname} , review:{review}, product_id : {product_id}")




            Product_Review.objects.create(
                review_user_id = request.user,
                review_product_id = product,
                message = review )

    return render(request,'productPreview.html')