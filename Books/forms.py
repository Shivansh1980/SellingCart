from .models import Book
from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# this Form.py creates a page requesting form from the user on the browser
# To use it import this in views.py and then 

# we will use this as a default user wihle using UserRegistrationForm

class BookForm(forms.ModelForm):
    class Meta: # this meta class is used to specify the model
        model = Book
        fields = {'title','author','pdf'}






