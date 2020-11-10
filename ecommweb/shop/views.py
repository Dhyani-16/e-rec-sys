from django.shortcuts import render
from django.http import HttpResponse
from .models import Product_Detail,Order_detail,Rating_Detail,Product_Review,UsersQuery
from math import ceil

# Create your views here.

def shopHome(request):
    allProducts = []
    catProds = Product_Detail.objects.values('category') #Getting Objects from the database..by using model product_detail category
    # print(catProds)
    cats = {item['category'] for item in catProds} #Getting the each obj category and store it in the set to get only unique categories
    for cat in cats:
        p = Product_Detail.objects.filter(category = cat) #it'll return the list of objects as requested.
        l = len(p)
        nslides = l//3 + ceil((l/3)-(l//3))
        allProducts.append([p, range(1, nslides), nslides])

    return render(request,'Home.html',{'AllProds':allProducts})


def cart(request):
    return render(request,'cart.html')

def contact(request):
    print("---")
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def productPreview(request,product_id):

    reviews = Product_Review.objects.filter(review_product_id=product_id)
    
    context = {'current_product_id' : product_id, 'review' : reviews}

    if request.method=="POST":
        
        #uname= request.POST.get('uname', '')
        #rating = request.POST.get('rating', rating)
        #product_id = request.POST.get('product_id', '')

        product = Product_Detail.objects.filter(product_id=product_id)[0]
        print("Product id",product)
        
        if request.POST['formtype'] == "rating":
           
            rating = request.POST['rating']
            product_id = product
            print(f"rating :{rating}, product_id : {product_id}")

            Rating_Detail.objects.create(
                rating_user_id = request.user,
                rating_product_id= product_id,
                rating = rating
            )
            
        elif request.POST['formtype']=='review':
            review = request.POST['review']
            print(f"review:{review}, product_id : {product_id}")

            Product_Review.objects.create(
                review_user_id = request.user,
                review_product_id = product,
                message = review )

   
    return render(request,'productPreview.html' , context=context)