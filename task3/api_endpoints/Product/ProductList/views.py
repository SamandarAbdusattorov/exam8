from cryptography.hazmat.primitives.ciphers.algorithms import AES
from rest_framework import generics, status
from rest_framework.response import Response
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from base64 import b64encode, b64decode

from task3.api_endpoints.Product.ProductList.renders import serialize
from task3.api_endpoints.Product.ProductList.serializer import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from task3.models import Product


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        return ProductSerializer 

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = []

        for product in queryset:
            serialized_product = product.serialize()
            serialized_data.append(serialized_product)

        return Response(serialized_data)


__all__ = ['ProductListAPIView']
