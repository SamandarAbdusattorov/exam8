from django.urls import path

from task2.api_endpoints.Vacancy.VacancyFilter.views import VacancyFilterAPIView

urlpatterns = [
    path("vacancy-filter/", VacancyFilterAPIView.as_view()),
]