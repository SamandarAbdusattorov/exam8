from rest_framework.serializers import ModelSerializer

from task1.models import User


class UserDestroySerializer(ModelSerializer):
    def delete(self, validated_data):
        validated_data["is_deleted"] = True
        return validated_data

    class Meta:
        model = User
        fields = ["username", "password"]
