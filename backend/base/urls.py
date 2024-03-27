from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_routes,name='routes' ),
    path('products/',views.products_list_api_view,name='products' ),
    path('product/<str:pk>/',views.products_detail_api_view,name='product' ),
]