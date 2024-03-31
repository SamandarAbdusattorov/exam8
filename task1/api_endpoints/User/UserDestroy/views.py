from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from task1.api_endpoints.User.UserDestroy.serializers import UserDestroySerializer
from task1.models import User


class UserDestroyView(APIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer

    def get_serializer_class(self):
        return UserDestroySerializer

    @action(detail=True, methods=["delete"], url_path="delete-user")
    def delete_user(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_deleted = True
        user.save()
        return Response(
            data={"detail": "User deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def delete(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        user.is_deleted = True
        user.save()
        return Response(
            data={"detail": "User deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )


__all__ = ["UserDestroyView"]
