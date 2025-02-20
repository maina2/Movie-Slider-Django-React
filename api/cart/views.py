from rest_framework import generics, permissions
from .models import Cart
from .serializers import CartSerializer
from products.models import Product

# View to list and create cart items
class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Return cart items for the logged-in user
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user when creating a cart item
        serializer.save(user=self.request.user)

# View to retrieve, update, and delete a specific cart item
class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        # Return cart items for the logged-in user
        return Cart.objects.filter(user=self.request.user)