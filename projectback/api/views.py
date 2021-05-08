from api.models import Product, Category
from django.http.response import JsonResponse
from api.serializers import CategoryModelSerializer, ProductSerializer, CartSerializer, UserModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


def product_list(request):
    product = Product.objects.all()
    product_json = [product.to_json() for product in product]
    return JsonResponse(product_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(product.to_json())


def category_list(request):
    category = Category.objects.all()
    category_json = [category.to_json() for category in category]
    return JsonResponse(category_json, safe=False)


@api_view(['GET', 'POST'])
def product2_list(request):
    if request.method == 'GET':
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"status": "500"}, safe=False)
    if request.method == 'POST':
        try:
            category = Category.objects.get(name=request.data['category'])
        except:
            return JsonResponse({"status": "200"}, safe=False)
        Product.objects.create(
            category=category,
            name=request.data['name'],
            description=request.data['description'],
            image=request.data['image'],
            price=request.data['price']
        )
        return JsonResponse({"status": "200"}, safe=False)


@api_view(['GET', 'POST'])
def category2_list(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            serializer = CategoryModelSerializer(categories, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({"status": "505"}, safe=False)
    if request.method == 'POST':
        try:
            category = Category.objects.get(name=request.data['category'])
            serializer = CategoryModelSerializer(category, many=True)
            return JsonResponse(serializer.data, safe=False)
        except:
            return JsonResponse({'status': '200'}, safe=False)


class ProductViewSet(APIView):
    @staticmethod
    def get(request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProductDetailViewSet(APIView):
    @staticmethod
    def get(request, pk):
        queryset = Product.objects.get(id=pk)
        serializer = ProductSerializer(queryset, many=False)
        return Response(serializer.data)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)
# def get(request):
#     queryset = Product.objects.all()
#     serializer = ProductSerializer(queryset, many=True)
#     return Response(serializer.data)
#
#
# class ProductViewSet(APIView):
#     pass
#
#
# def get(request, pk):
#     queryset = Product.objects.get(id=pk)
#     serializer = ProductSerializer(queryset, many=False)
#     return Response(serializer.data)
#
#
# class ProductDetailViewSet(APIView):
#     pass
