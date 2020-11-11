from django.urls import path,include
from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


admin.site.site_header="Ecommerce Web Admin Site"
admin.site.site_title="Ecommerce Website"
admin.site.index_title="Ecommerce Website"


urlpatterns = [
    path("",views.shopHome,name="shopHome"),
    path("about/",views.about,name="About"),
    path("contact/",views.contact,name="Contact"),
    path("cart/",views.cart,name="Cart"),
    path("productDetail/<int:product_id>",views.productPreview,name="ProductDetail"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root = settings.MEDIA_ROOT)