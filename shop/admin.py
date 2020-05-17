from django.contrib import admin
from . models import Product, CartItem, OrderedProduct
# Register your models here.
# your data in the database of admin pannel will not shown untill you do not register them
# To create the user for admin site you will use the command python manage.py createsuperuser whicn in turn ask for new username and password

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(OrderedProduct)
