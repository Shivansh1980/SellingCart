from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Book
from django import forms
from django.core.files.storage import FileSystemStorage
from .forms import BookForm , CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url ="login")
def book_list(request):
    book = Book.objects.all()
    params = {'books':book}
    return render(request , 'books/BookHomePage.html',params)

@login_required(login_url ="login")
def book_upload(request):
    if(request.method == 'POST'):
        form = BookForm(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('book_list')
    else :
        form = BookForm()
    return render(request , 'books/BookUpload.html' , {'form':form})

def registration_form(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        print('working')
        if form.is_valid():
            form.save()
            return redirect('login')
        else :
            print("Form is not valid")
    else:
        form = CreateUserForm()
    return render(request ,'books/registration/registration.html',{'form':form})

def login_form(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('ShopHome')
    return render(request, 'books/registration/login.html')

