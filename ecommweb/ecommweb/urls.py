
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')) # redirect to the urls.py file in shop app
]
