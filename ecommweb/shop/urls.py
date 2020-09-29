from django.urls import path
from . import views

urlpatterns = [
    path('product',views.productPreview , name='product'),
    path('/',views.Home,name='Home),
]
