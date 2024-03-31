from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from task1.api_endpoints.User.UserLogin.serializer import UserLoginSerializer
from task1.models import User


class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        pk = serializer.validated_data.get("pk")
        user = User.objects.get(username=username)
        if user.is_deleted == True:
            return Response(
                {"message": "User cannot login "}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(data=serializer.data, status=status.HTTP_200_OK)


__all__ = [
    "UserLoginAPIView",
]
