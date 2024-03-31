from django.urls import path

from task3.api_endpoints.Product import ProductListAPIView
from task3.api_endpoints.Product.ProductCreate.views import ProductCreateAPIView

urlpatterns = [
    path("product-list/", ProductListAPIView.as_view()),
    path("product-create/", ProductCreateAPIView.as_view())
]