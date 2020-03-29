from django.contrib import admin
from django.urls import path
from . import views
# Django will First see the urls of our main file of urls.py which is in Selling Cart Folder
# From there it will read the site in the include function and will redirect it to this urls.py accordingly the page will be displayed

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUS"),
    path("contact/",views.contact,name="ContactUS"),
    path("productview/",views.productview,name="Productview"),
    path("search/",views.search,name="search"),
    path("tracker/",views.tracker,name="tracker"),
    path("checkout/",views.checkout,name="checkout"),
]