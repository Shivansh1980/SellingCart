from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.models import Product
from .serializers import ProductSerializer
