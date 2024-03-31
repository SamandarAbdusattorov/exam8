from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from task2.models import Vacancy
from task2.api_endpoints.Vacancy.VacancyFilter.serializers import VacancySerializer

class VacancyFilterAPIView(APIView):
   def get(self, request):
        salary_from = request.query_params.get('salary_from')
        salary_to = request.query_params.get('salary_to')
        salary = request.query_params.get("salary")
        
        if salary is not None:
            vacancies = Vacancy.objects.filter(salary=salary)
        elif salary_from is not None and salary_to is not None:
            vacancies = Vacancy.objects.filter(salary_from__lte=salary_to, salary_to__gte=salary_from)
        else:
            vacancies = Vacancy.objects.all()
        
       
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

__all__ = ['VacancyFilterAPIView']