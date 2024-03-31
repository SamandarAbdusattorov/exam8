from task1.models import User

# serializers.py
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password")
