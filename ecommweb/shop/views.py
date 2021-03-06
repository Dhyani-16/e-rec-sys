from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product_Detail,Order_detail,Rating_Detail,Product_Review,UsersQuery, Wishlist
from math import ceil
from Authentication.models import Profile
from django.db.models import Q
from django.contrib import messages
from datetime import datetime,timedelta
import json

# Create your views here.

def shopHome(request):

    context = {}
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        
        if (request.method=='POST' and 'value' in request.POST.keys()):
            saveCartForProfile(request.POST['value'] , profile)
            print(profile.mycart)
        
        context['mycart'] = json.dumps(profile.mycart)


    allProducts = []
    catProds = Product_Detail.objects.values('category') #Getting Objects from the database..by using model product_detail category
    # print(catProds)
    cats = {item['category'] for item in catProds} #Getting the each obj category and store it in the set to get only unique categories
    for cat in cats:
        p = Product_Detail.objects.filter(category = cat)[:15] #it'll return the list of objects as requested.
        l = len(p)
        nslides = l//3 + ceil((l/3)-(l//3))
        allProducts.append([p, range(1, nslides), nslides])

    context['AllProds'] = allProducts

    return render(request,'Home.html',context)

def saveCartForProfile(c,profile):
    profile.mycart = c
    profile.save()

def category(request,cat):

    prods = Product_Detail.objects.filter(category=cat)

    return render(request, 'category.html', {'AllProds': prods,'category':cat,'totalProds':len(prods)})

def cart(request):
    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user=request.user)
        print(user_profile.default_address_value)  
        context={'profile':user_profile,'defaultAdd':user_profile.default_address_value}
        if request.method=="POST":

            if 'value' in request.POST.keys():
                saveCartForProfile(request.POST['value'],user_profile)
                print(user_profile.mycart)
            
            else:   
                amount = request.POST['amount'] 
                pi = request.POST['product_ids']
                product_ids = json.loads(pi)
                q = request.POST['quantity']
                qty = json.loads(q)
                print(f"amount :{amount},product_ids:{product_ids}")
                print(qty)

                

                Order_detail.objects.create(
                    order_user_id=request.user,
                    product_ids=product_ids,
                    amount=amount,
                    order_date=datetime.now(),
                    delivery_date=datetime.now()+timedelta(days=5),
                )
                count=0
                for i in product_ids:
                    product = Product_Detail.objects.get(product_id=i)
                    # print(product.quantity)
                    product.quantity = product.quantity - qty[count]
                    product.save()
                    count= count+1
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
    context = {'current_product_id' : product_id, 'review' : reviews, 'products' : products,
    'questions':questions }
    
    if (request.user.is_authenticated):

        wishlist_prod = Wishlist.objects.filter(wishlist_user_id=request.user).values_list('wishlist_product_id', flat=True)[:]
        
        
        x = Profile.objects.get(user=request.user)
        
        dict = {}
        for i in wishlist_prod:
            dict[i]=1
            
        context['wishlist_prod'] = list(dict.keys())
        
        
        if request.method=="POST":
            
            print("Product id",products)
            product_id = products
            
            # check if request.POST contains formtype key or not 
            if 'formtype' in request.POST.keys():
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

            else:
                saveCartForProfile(request.POST['value'],x)
                print(x.mycart)
    
   
    return render(request,'productPreview.html' , context=context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        product = Product_Detail.objects.all().filter(Q(product_name__icontains=search) | Q(description__icontains=search) | Q(brand__icontains=search))

        context={'product':product,'search':search,'totalProds':len(product)}
        return render(request, 'search.html',context=context)
        
    