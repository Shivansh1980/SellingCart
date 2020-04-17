from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Book
from django import forms
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q



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
    
@login_required(login_url ="login")
def search_book(request):
    if request.method == "GET":
        srch = request.GET.get('search_book')
        book = Book.objects.all().filter(Q(title__icontains = srch) | Q(author__icontains = srch))
        params = {'books':book}
        return render(request , 'books/BookHomePage.html',params)
