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
            rating = request.POST['rating']
            print(f"username:{request.user} , Rating :{rating}, product_id : {product}")

            Rating_Detail.objects.create(
                rating_user_id = request.user,
                rating_product_id= product,
                rating = rating
            )
            
        elif request.POST['formtype']=='review':
            review = request.POST['review']
            print(f"username:{request.user} , Review:{review}, product_id : {product}")

            Product_Review.objects.create(
                review_user_id = request.user,
                review_product_id = product,
                message = review )

    return render(request,'productPreview.html')