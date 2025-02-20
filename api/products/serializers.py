from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()  # Shows category name instead of ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Allow category ID

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
