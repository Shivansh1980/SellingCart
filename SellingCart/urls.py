"""SellingCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from api.viewset import ProductModelViewSet

router = DefaultRouter()
#now we will register product viewset with router
router.register('productapi',ProductModelViewSet,basename='student')


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('shop.urls')),
    path('shop/', include('shop.urls')),
    path('books/',include('Books.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', TemplateView.as_view(template_name = 'index.html'),name='Profile'),
    path("api/",include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
