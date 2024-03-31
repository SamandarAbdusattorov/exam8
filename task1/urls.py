from django.urls import path

from task1.api_endpoints.User import (
    UserRegisterView,
    UserDestroyView,
    UserLoginAPIView,
)

urlpatterns = [
    path("user-register/", UserRegisterView.as_view()),
    path("user-delete/<int:pk>", UserDestroyView.as_view()),
    path("user-login/", UserLoginAPIView.as_view()),
]
