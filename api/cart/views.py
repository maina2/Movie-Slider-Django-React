from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer
from products.models import Product
from django.shortcuts import get_object_or_404

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = get_object_or_404(Product, id=product_id)
        quantity = request.data.get('quantity', 1)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.quantity = request.data.get('quantity', cart_item.quantity)
        cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)
