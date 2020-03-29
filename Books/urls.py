from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.book_list,name="book_list"),
    path("upload/",views.book_upload,name="uploadbooks"),
    path("registration/",views.registration_form,name="registration"),
    path("login/",views.login_form,name="login"),
    path("logout/",views.logout_file,name="logout"),
    path("search/",views.search_book,name="search_book"),
]