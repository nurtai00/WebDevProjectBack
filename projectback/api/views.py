from api.models import Product, Category, Cart, User
from django.http.response import HttpResponse, JsonResponse

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse, HttpResponse
from api.models import Category, Product, Cart, User
from api.serializers import CategorySerializer, ProductSerializer, CartSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core import serializers


# def product_list(request):
#     product = Product.objects.all()
#     product_json = [product.to_json() for product in product]
#     return JsonResponse(product_json, safe=False)
#
#
# def product_detail(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist as e:
#         return JsonResponse({'message': str(e)}, status=400)
#     return JsonResponse(product.to_json())
#
#
# def category_list(request):
#     category = Category.objects.all()
#     category_json = [category.to_json() for category in category]
#     return JsonResponse(category_json, safe=False)

def get(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


class ProductViewSet(APIView):
    pass


def get(request, pk):
    queryset = Product.objects.get(id=pk)
    serializer = ProductSerializer(queryset, many=False)
    return Response(serializer.data)


class ProductDetailViewSet(APIView):
    pass
