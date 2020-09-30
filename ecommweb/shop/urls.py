from django.urls import path
from Shop import views

urlpatterns = [
    path("",views.shopHome,name="shopHome"),
    path("about/",views.about,name="About"),
    path("contact/",views.contact,name="Contact"),
    path("cart/",views.cart,name="Cart"),
    path("productDetail/",views.productPreview,name="ProductDetail"),
]
