from django.shortcuts import render , redirect
from .models import Product
from math import ceil
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# import Q is used for the search functionality here Q accepts the parameter 
# that are available in the models.py with __icontains as extension and search that 
# in databaase if exists

from django.db.models import Q 
@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    params = {'product': products}
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

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")