from abc import ABC

from rest_framework import serializers
from api.models import Category, Product, Cart, User


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')


class CartSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Cart
        fields = ('username', 'address', 'book')


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
