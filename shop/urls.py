from django.contrib import admin
from django.urls import path
from . import views
# Django will First see the urls of our main file of urls.py which is in Selling Cart Folder
# From there it will read the site in the include function and will redirect it to this urls.py accordingly the page will be displayed

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("contact/",views.contact,name="ContactUS"),
    path("productview/<int:id>",views.productview,name="product_view"),
    path("search/",views.search,name="search"),
    path("tracker/",views.tracker,name="tracker"),
    path("checkout/",views.checkout,name="checkout"),
    path("add_to_cart/",views.addtocart,name='addtocart'),
    path("viewcart/",views.view_cart,name='cartview'),
    path("delete_item/<int:pid>", views.delete_item, name='deleteitem'),
    path("orderinfo/<int:pid>", views.order_info_page, name='orderinfo'),
    path("order_from_cart/", views.order_from_cart, name='orderfromcart'),
    path("order_cart_items/", views.place_order_of_cart_item,name='ordercartitems'),
]
