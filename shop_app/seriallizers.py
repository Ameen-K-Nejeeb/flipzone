from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.MolelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "slug", "image", "description", "category", "price"]
