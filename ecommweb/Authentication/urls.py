from django.urls import path,include
from . import views

urlpatterns = [

    path("sign_up/",views.SignupUSER,name="SignupUSER"),
    path("log_in/",views.LoginUSER,name="LoginUSER"),
    path("log_out/",views.LogoutUSER,name="LogoutUSER"),

    path("account/",views.account,name="Account"),
    path("add_address",views.add_address,name="Add_address"),

    path("account_settings_1/",views.account_settings_1,name="Account_settings_1"),    
    path("account_settings_2/",views.account_settings_2,name="Account_settings_2"),

    path("set_default_address/",views.set_default_address,name="set_default_address"),
    path("deleteAd/<int:objId>/delete",views.deleteAd,name="deleteAd"),
    
]