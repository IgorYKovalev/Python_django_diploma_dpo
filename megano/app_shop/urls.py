from django.urls import path
from app_shop.api import CategoryListView, ProductListView, ProductFullListView, TagListView

app_name = "app_shop"

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('banners/', ProductListView.as_view(), name='banners'),
    path('products/popular/', ProductListView.as_view(), name='products'),
    path('products/limited/', ProductListView.as_view(), name='products'),
    path('product/<int:id>', ProductFullListView.as_view(), name='product'),
    path('tags/', TagListView.as_view(), name='tags'),
    # path('products/<int:id>/', ProductListView.as_view(), name='products'),
]
