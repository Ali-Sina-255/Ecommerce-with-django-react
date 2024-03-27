from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from base.Api.serializers import ProductSerializers

from . models  import Product

@api_view(['GET', 'PUT'])
def get_routes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<int:id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<int:id>/',
        '/api/products/<update>/<int:id>/',
    ]
    return Response(routes)



@api_view(['GET'])
def products_list_api_view(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def products_detail_api_view(request, pk):
    try:
        product_detail =Product.objects.get(_id=pk)
        serializer = ProductSerializers(product_detail, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"message":f"Product with is id {pk} is not in the database!"},status=status.HTTP_404_NOT_FOUND)