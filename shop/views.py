from django.shortcuts import render , redirect
from .models import Product, CartItem
from .forms import OrderInfo
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q,Max,Sum
from channels.routing import ProtocolTypeRouter

# import Q is used for the search functionality here Q accepts the parameter 
# that are available in the models.py with __icontains as extension and search that (Read more about this at last of your java copy)
# in databaase if exists

from django.db.models import Q 
global no_of_items
@login_required(login_url='login')
def index(request):
    cart_items = CartItem.objects.filter(customer_name=request.user)
    max_item_dict = cart_items.aggregate(Sum('item_quantity'))
    no_of_items = 0
    if (max_item_dict['item_quantity__sum'] == None):
        no_of_items = 0
    else:
        no_of_items = max_item_dict['item_quantity__sum']
    products = Product.objects.all()
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
def addtocart(request):
    product = None
    if (request.method == "GET"):
        productid = request.GET['id']
        requested_product = Product.objects.get(id=productid)
        customer_products = CartItem.objects.filter(Q(customer_name=request.user) & Q(product_detail=requested_product))
        if(customer_products.exists()):
            product = customer_products.get(Q(product_detail = requested_product))
        if (product):
            product.item_quantity += 1
            product.save()
        else:
            newitem = CartItem(customer_name=request.user, item_quantity=1, product_detail=requested_product)
            newitem.save()
        dictionary = CartItem.objects.filter(Q(customer_name=request.user)).aggregate(Sum('item_quantity'))
        return HttpResponse(dictionary['item_quantity__sum'])

@login_required(login_url='login')
def delete_item(request,pid):
    item = CartItem.objects.filter(Q(product_detail_id=pid) & Q(customer_name=request.user))
    item.delete()
    return redirect('cartview')

@login_required(login_url='login')
def view_cart(request):
    products = CartItem.objects.all().filter(customer_name=request.user)
    dictionary = CartItem.objects.filter(Q(customer_name=request.user)).aggregate(Sum('item_quantity'))
    no_of_items = dictionary['item_quantity__sum']
    dictionary = CartItem.objects.filter(Q(customer_name=request.user))
    price = 0
    cart = []
    for p in dictionary:
        price += p.product_detail.price*p.item_quantity
    for i in products:
        cart.append(i)
    params = { 'product':cart,'items_count':no_of_items,'price':price}
    return render(request, 'shop/Cart.html', params)

@login_required(login_url='login')
def order_info_page(request,pid):
    form = OrderInfo()
    params = {'form': form,'id':pid}   
    return render(request , 'shop/order/orderform.html', params)

@login_required(login_url='login')
def order_placed(request,pid):
    return redirect('shop/order/orderplaced.html') 
