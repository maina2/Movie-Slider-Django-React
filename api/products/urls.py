from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, CategoryProductsView

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),  # Include ViewSet routes
    path('categories/<int:category_id>/products/', CategoryProductsView.as_view(), name='category-products'),
]
