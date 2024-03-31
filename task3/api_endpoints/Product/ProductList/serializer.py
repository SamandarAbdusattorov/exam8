# from cryptography.fernet import Fernet
# from rest_framework.fields import DecimalField, CharField
from rest_framework.serializers import ModelSerializer
from task3.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["title", "price", "package_code", "marja"]
