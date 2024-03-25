from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . products import products


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
    return Response(products)



@api_view(['GET'])
def products_detail_api_view(request, value_from_url):
    product = products
    for pro in products:
        if pro['_id'] == value_from_url:
            product = pro
            break
        
    return Response(product)