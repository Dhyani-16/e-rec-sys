from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=100)
    first_name2 = models.CharField(max_length=100, blank=True,default="")
    
    last_name = models.CharField(max_length=100, blank=True)
    last_name2 = models.CharField(max_length=100, blank=True,default="")

    contact_no = models.BigIntegerField() 
    contact_no2 = models.BigIntegerField( blank=True,default=11111111)  
    
    address1 = models.TextField(max_length=10000,default="")
    address2 = models.TextField(max_length=10000,blank=True,default="")
    
    CITY_CHOICES = [
        ('Ahmedabad', 'Ahmedabad'),
        ('Surat', 'Surat'),
        ('Rajkot', 'Rajkot'),
        ('Gandhinagar', 'Gandhinagar'),
        ('Bhavnagar', 'Bhavnagar'),
    ]
    city = models.CharField(
        max_length=50,
        choices=CITY_CHOICES,
        default='Ahmedabad',
    )
    city2 = models.CharField(
        max_length=50,
        choices=CITY_CHOICES,
        default='Ahmedabad', blank=True
    )

    state = models.CharField(max_length=100)
    state2 = models.CharField(max_length=100, blank=True,default="")
    
    pincode = models.PositiveIntegerField()
    pincode2 = models.PositiveIntegerField( blank=True,default=111111)

    default_address_value = models.IntegerField(default=1)
    mycart = models.CharField(max_length=5000,blank=True,default="{}")


    def __str__(self):
        return self.user.username
