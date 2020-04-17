from django.shortcuts import render , redirect
from .models import Product ,CartItems
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# import Q is used for the search functionality here Q accepts the parameter 
# that are available in the models.py with __icontains as extension and search that (Read more about this at last of your java copy)
# in databaase if exists

from django.db.models import Q 

@login_required(login_url='login')
def index(request):
    no_of_items = CartItems.objects.filter(customer_name=request.user).count()
    products = Product.objects.all()
    print(products[0].id)
    params = {'product': products,'items_count':no_of_items}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    if(request.method == "GET"):
        cat = request.GET.get('search')
        products = Product.objects.all().filter(Q(category__icontains = cat) | Q(product_name__icontains = cat))
        if products is None:
            print('No Product Found')
    return render(request,'shop/index.html',{'product':products})

@login_required(login_url='login')
def productview(request,id):
    print(request.user)
    product = Product.objects.filter(id=id)
    context = {'product':product}
    return render(request,'shop/productView.html',context)

@login_required(login_url='login')
def checkout(request,myid):
    return HttpResponse('This is the checkout Page')

@login_required(login_url='login')
def add_to_cart(request , pid):
    cart = CartItems(
            item_name=Product.objects.get(id=pid).product_name,
            item_id = pid,
            item_image = Product.objects.get(id=pid).image,
            customer_name = request.user,

            )
    cart.save()
    return redirect('ShopHome')

@login_required(login_url='login')
def delete_item(request,pid):
    item = CartItems.objects.filter(Q(item_id=pid) & Q(customer_name=request.user))
    item.delete()
    return redirect('cartview')

@login_required(login_url='login')
def view_cart(request):
    cart = CartItems.objects.all().filter(customer_name=request.user)
    params = { 'product':cart }
    return render(request,'shop/Cart.html',params)