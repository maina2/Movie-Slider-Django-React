from rest_framework import serializers
from .models import Cart
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()  

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity', 'added_at', 'total_price']
        read_only_fields = ['id', 'added_at', 'total_price']  
    def get_total_price(self, obj):
        return obj.total_price() 