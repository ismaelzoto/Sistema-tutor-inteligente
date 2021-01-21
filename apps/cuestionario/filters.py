import django_filters
from apps.sistema.models import cuestionario

class cuestionarioFilter(django_filters.FilterSet):
    class Meta:
        model = cuestionario
        fields = ['id_cuestionario','id_pregunta_test']