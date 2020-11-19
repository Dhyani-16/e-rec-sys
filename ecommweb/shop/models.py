from django.db import models

# Get User model.
from django.contrib.auth.models import User
import jsonfield

class Product_Detail(models.Model):
    
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    product_specification = jsonfield.JSONField()
    img1 = models.ImageField(upload_to="shop/images")
    img2 = models.ImageField(upload_to="shop/images",blank=True)
    img3 = models.ImageField(upload_to="shop/images",null=True,blank=True)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    
    categoryid = models.CharField(max_length=50)
    categories_choices = (('Clothing','Clothing'),('Accessories','Accessories'),('Electronics','Electronics'),('Footwear','Footwear'),('Grocery','Grocery'))
    category = models.CharField(max_length=50,choices=categories_choices,default="Clothing")
    
    productrating = models.FloatField()
    # rating = {
    #         ('1' , '1'),
    #         ('2' , '2'),
    #         ('3' , '3'),
    #         ('4' , '4'),
    #         ('5' , '5')
    #     }

    # productrating =models.CharField(max_length=100,choices=rating,default='3')

    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product_id)

class Order_detail(models.Model):
    order_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_ids = models.TextField(default="",max_length=1000)        

    order_id = models.AutoField(primary_key=True)
    amount = models.FloatField(default=0.0)
    delivery_date = models.DateField(default="")
    order_date = models.DateField(auto_now_add=True)
    
    ORDER_STATUS = (
        ('delivered','Delivered'),
        ('pending','Pending')
    )
    status =models.CharField(max_length=100,choices=ORDER_STATUS,default='pending')
    
    product_data = jsonfield.JSONField()
    
    def __str__(self):
        return self.order_id

class Rating_Detail(models.Model):
        rating_user_id = models.ForeignKey(User,on_delete=models.CASCADE, default='0')
        rating_product_id = models.ForeignKey(Product_Detail, on_delete=models.CASCADE, default='1')
        #, related_name='product_id'
        srNo = models.AutoField(primary_key=True)

        rating_star = {
            ('1' , '1'),
            ('2' , '2'),
            ('3' , '3'),
            ('4' , '4'),
            ('5' , '5')
        }

        rating =models.CharField(max_length=100,choices=rating_star,default='3')

        def __str__(self):
            obj = f"{self.rating} By {self.rating_user_id} for {self.rating_product_id}" 
            return obj

class Product_Review(models.Model):
        review_user_id = models.ForeignKey(User,on_delete=models.CASCADE, default="0")
        review_product_id = models.ForeignKey(Product_Detail,on_delete=models.CASCADE, default='1')
        
        srNo = models.AutoField(primary_key=True)
        message = models.CharField(max_length=300, default='-')
        reviewTime = models.DateTimeField(auto_now_add=True)    

        def __str__(self):
            return f"{self.review_user_id} Reviewed On a {self.review_product_id} at {self.reviewTime}"

class UsersQuery(models.Model):
        query_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
        query_product_id = models.ForeignKey(Product_Detail,on_delete=models.CASCADE)
        
        srNo = models.AutoField(primary_key=True)
        question = models.CharField(max_length=500)
        currentTime = models.DateTimeField(auto_now_add=True)
        answer = models.CharField(max_length=500)
        likes = models.IntegerField()

        def __str__(self):
            return f"{self.query_user_id} Has Query Regarding {self.query_product_id}"
        