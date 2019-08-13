import django_filters
from apps.sistema.models import inteligencias

class inteligenciasFilter(django_filters.FilterSet):
    class Meta:
        model = inteligencias
        fields = ['id_inteligencias','tipo_de_inteligencia']