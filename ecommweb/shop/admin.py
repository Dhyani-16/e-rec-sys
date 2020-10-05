from django.contrib import admin

# Register your models here.
from .models import Product_Detail,Order_detail,Rating_Detail,Product_Review,UsersQuery

admin.site.register(Product_Detail)
admin.site.register(Order_detail)
admin.site.register(Rating_Detail)
admin.site.register(Product_Review)
admin.site.register(UsersQuery)