from django.shortcuts import render , redirect
from .models import Product, CartItem
from .models import OrderedProduct as OrderInfo
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q,Max,Sum
import json, requests, math, random, os
from SellingCart import settings

# import Q is used for the search functionality here Q accepts the parameter 
# that are available in the models.py with __icontains as extension and search that (Read more about this at last of your java copy)
# in databaase if exists

from django.db.models import Q 
global no_of_items
@login_required(login_url='login')
def index(request):
    product_category_text = os.path.join(settings.BASE_DIR, "shop\product_categories.txt")
    f = open(product_category_text, 'r')
    categories_list = f.readlines()

    cart_items = CartItem.objects.filter(customer_name=request.user)
    max_item_dict = cart_items.aggregate(Sum('item_quantity'))
    no_of_items = 0
    if (max_item_dict['item_quantity__sum'] == None):
        no_of_items = 0
    else:
        no_of_items = max_item_dict['item_quantity__sum']
    products = Product.objects.all()
    categories = list()
    for category in categories_list:
        newlist = []
        for pr in products:
            if pr.category.lower() == category.lower().strip():
                newlist.append(pr)

        if len(newlist) != 0:
            categories.append(newlist)

    params = {'categories': categories,'items_count':no_of_items}
    return render(request, 'shop/home.html', params)

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    products = list()
    if (request.method == "GET"):
        cat = request.GET['search']
        products = Product.objects.all().filter(Q(category__icontains = cat) | Q(product_name__icontains = cat))
        if products is None:
            print('No Product Found')
    return render(request,'shop/home.html',{'product':products})

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
def order_from_cart(request):
    products = CartItem.objects.all().filter(customer_name=request.user)
    ordered_item = []
    for i in products:
        ordered_item.append(i)
    price = int(0)
    for i in ordered_item:
        price += i.product_detail.price
    print(products)
    print(ordered_item)
    details_of_product = {'product': ordered_item, 'price': price}
    return render(request, "shop/order/cartorderform.html", details_of_product)


def place_order_of_cart_item(request):
    products = CartItem.objects.all().filter(customer_name=request.user)
    product = []
    for i in products:
        items = Product.objects.get(id=i.product_detail.id)
        product.append(items)
    print("Products which are going to be order : ", product)
    
    if (request.method == "POST"):
        a1 = request.POST['address1']
        a2 = request.POST['address2']
        phone = request.POST['phone']
        state = request.POST['state']
        mode = request.POST['mode']
        for item in product:
            order_details = OrderInfo(
                customer_name=request.user,
                address1=a1,
                address2=a2,
                state=state,
                mobile_no=phone,
                dilevery_mode=mode,
                product=item,
                status="active"
            )
    params = {'product': product}
    return render(request, "shop/order/orderplaced.html", params)

#ordeinfo page means the product which is going to order page. This will be called when User click on
# Order button on the form page.
@login_required(login_url='login')
def order_info_page(request, pid):
    params = {'id':pid}
    print("inside order info page")
    if (request.method == "POST"):
        a1 = request.POST['address1']
        a2 = request.POST['address2']
        phone = request.POST['phone']
        state = request.POST['state']
        mode = request.POST['mode']

        product = list()
        product.append(Product.objects.get(id=pid))
        
        order_details = OrderInfo(
            customer_name=request.user,
            address1=a1,
            address2=a2,
            state=state,
            mobile_no=phone,
            dilevery_mode=mode,
            product=Product.objects.get(id=pid),
            status="active"
            )

        #ucomment the below line to save the order details
        #order_details.save()
        print("product has been saved")
        params = {'product':product,'id': pid}
        return render(request, 'shop/order/orderplaced.html', params)
    return render(request, 'shop/order/orderform.html',params)

