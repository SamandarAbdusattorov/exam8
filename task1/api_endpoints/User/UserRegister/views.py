from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from task1.api_endpoints.User.UserRegister.serializers import (
    UserRegisterSerializer,
)
from task1.models import User


class UserRegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, reqeust):
        serializer = UserRegisterSerializer(data=reqeust.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        username = reqeust.data["username"]
        user = User.objects.get(username=username)

        if user.is_deleted == True:
            user.is_deleted = False
            user.save()
            return Response(
                {"message": "User successfully created"}, status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ["UserRegisterView"]
