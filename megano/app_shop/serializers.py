from rest_framework import serializers
from app_shop.models import Category, Subcategories, Product, Review, Tag, ImageProduct, Specification


class CustomField(serializers.Field):
    def to_representation(self, value):
        ret = {
            'src': str(value.url),
            'alt': str(value.name)
        }
        return ret


class SubcategoriesSerializer(serializers.ModelSerializer):
    image = CustomField()

    class Meta:
        model = Subcategories
        fields = [
            'id',
            'title',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    image = CustomField()
    subcategories = SubcategoriesSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'image',
            'subcategories',
        ]


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = [
            'src',
            'alt',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageProductSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'price',
            'count',
            'date',
            'title',
            'description',
            'freeDelivery',
            'images',
            'tags',
            'reviews',
            'rating',
        ]


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = [
            'name',
            'value',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'author',
            'email',
            'text',
            'rate',
            'date',
        ]


class CustomProductField(serializers.Field):
    def to_representation(self, value):
        ret = [str(value.name)]
        return ret


class ProductFullSerializer(serializers.ModelSerializer):
    images = CustomProductField()
    tags = CustomProductField()
    reviews = ReviewSerializer(many=True, source='review')
    specifications = SpecificationSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'price',
            'count',
            'date',
            'title',
            'description',
            'fullDescription',
            'freeDelivery',
            'images',
            'tags',
            'reviews',
            'specifications',
            'rating',
        ]

