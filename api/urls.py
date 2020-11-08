from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("shop/getproducts",views.api_get_products,name="getproducts"),
]