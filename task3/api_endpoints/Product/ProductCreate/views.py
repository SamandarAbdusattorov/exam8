from cryptography.hazmat.primitives.ciphers.algorithms import AES
from task3.api_endpoints.Product.ProductCreate.serializer import ProductCreateSerializer

from rest_framework import generics
from task3.models import Product


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

__all__ = ['ProductCreateAPIView']
