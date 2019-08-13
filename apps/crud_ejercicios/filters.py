import django_filters
from apps.sistema.models import ejercicios

class ejerciciosFilter(django_filters.FilterSet):
    class Meta:
        model = ejercicios
        fields = ['nombre_ejercicio']