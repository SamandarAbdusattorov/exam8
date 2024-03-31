from rest_framework.serializers import ModelSerializer
from task2.models import Vacancy

class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['salary_from', 'salary_to', 'salary']