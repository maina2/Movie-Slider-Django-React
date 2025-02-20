from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Users can view, only admins can manage

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()


class CategoryProductsView(APIView):
    permission_classes = [AllowAny]  # Everyone can view categories and products

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)

        if not products.exists():
            return Response({"message": "No products found in this category"}, status=200)

        serializer = ProductSerializer(products, many=True)
        return Response({
            "category": category.name,
            "products": serializer.data
        })


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Users can view, only admins can manage

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdminUser()]
        return super().get_permissions()
