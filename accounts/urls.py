from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("registration/",views.registration_form,name="registration"),
    path("login/",views.login_form,name="login"),
    path("logout/",views.logout_file,name="logout"),
]