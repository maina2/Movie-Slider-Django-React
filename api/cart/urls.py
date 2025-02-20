from django.urls import path
from .views import CartListCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),
]