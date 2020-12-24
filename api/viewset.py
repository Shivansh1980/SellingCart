from rest_framework import viewsets
from shop.models import Product
from rest_framework import status
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    # def list(self, request):
    #     product = Product.objects.all()
    #     serializer = ProductSerializer(product, many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self, request, pk=None):
    #     id = pk
    #     if id is not None:
    #         pr = Product.objects.get(id=id)
    #         serializer = ProductSerializer(pr)
    #         return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Successfully Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def update(self, request, pk):
    #     id = pk
    #     pr = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(pr, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Successfully Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def partial_update(self, request, pk):
    #     id = pk
    #     pr = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(pr, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Data Successfully Updated'})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

