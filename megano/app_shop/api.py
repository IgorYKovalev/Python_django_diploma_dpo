from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app_shop.models import Category, Product, Tag
from app_shop.serializers import CategorySerializer, ProductSerializer, ProductFullSerializer, TagSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFullListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
