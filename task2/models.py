from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)