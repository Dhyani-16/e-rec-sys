from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product_Detail,Order_detail,Rating_Detail,Product_Review,UsersQuery, Wishlist
from math import ceil
from Authentication.models import Profile
from django.db.models import Q
from django.contrib import messages
from datetime import datetime

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
    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user=request.user)
        print(user_profile.default_address_value)  
        context={'profile':user_profile,'defaultAdd':user_profile.default_address_value}
        if request.method=="POST":
                
                amount = request.POST['amount']
                print(f"amount :{amount}")
                Order_detail.objects.create(
                    order_user_id=request.user,
                    amount=amount,
                    order_date=datetime.now(),
                    delivery_date=datetime.now(),
                )
        return render(request,'cart.html',context=context)

    return redirect('LoginUSER')

def contact(request):
    # print("---")
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def productPreview(request,product_id):

    products = Product_Detail.objects.filter(product_id=product_id)[0]
    
    questions = UsersQuery.objects.filter(query_product_id=product_id)
    
    reviews = Product_Review.objects.filter(review_product_id=product_id)

    field='body'

    wishlist_prod = Wishlist.objects.filter(wishlist_user_id=request.user).values_list('wishlist_product_id', flat=True)[:]

    dict = {}
    for i in wishlist_prod:
        dict[i]=1
        
    context = {'current_product_id' : product_id, 'review' : reviews, 'products' : products,
    'questions':questions, 'wishlist_prod' : list(dict.keys())
    }
    
    if request.method=="POST":
        
        print("Product id",products)
        product_id = products
        
        if request.POST['formtype'] == "rating":
           
            rating = request.POST['rating']
           
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
                review_product_id = product_id,
                message = review )


        elif request.POST['formtype']=="FAQ":
            q = request.POST['postquestion']
            
            UsersQuery.objects.create( query_product_id= products , 
                query_user_id = request.user,
                question=q,answer="",likes=0  )

        elif request.POST['formtype'] == "wishlist":
            x=int(request.POST['flag'])
            
            if x==1:
                Wishlist.objects.create(
                    wishlist_user_id = request.user,
                    wishlist_product_id= product_id,
                    #rating = rating
                )

            else:
                wishlist = Wishlist.objects.get(wishlist_user_id=request.user, wishlist_product_id=product_id)
                wishlist.delete()
   
    return render(request,'productPreview.html' , context=context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        product = Product_Detail.objects.all().filter(Q(product_name__icontains=search) | Q(description__icontains=search) | Q(brand__icontains=search))

        context={'product':product,'search':search}
        return render(request, 'search.html',context=context)
        
    