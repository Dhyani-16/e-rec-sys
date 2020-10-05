from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.shopHome,name="shopHome"),
    path("about/",views.about,name="About"),
    path("contact/",views.contact,name="Contact"),
    path("cart/",views.cart,name="Cart"),
    path("productDetail",views.productPreview,name="ProductDetail"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)