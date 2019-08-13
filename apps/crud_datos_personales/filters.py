import django_filters
from apps.sistema.models import datos_personales

class datospersonalesFilter(django_filters.FilterSet):
    class Meta:
        model = datos_personales
        fields = ['nombre','a_paterno','a_materno']