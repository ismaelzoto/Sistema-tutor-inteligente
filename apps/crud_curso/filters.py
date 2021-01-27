import django_filters
from apps.sistema.models import curso


class cursoFilter(django_filters.FilterSet):
    class Meta:
        model = curso
        fields= ['id_curso','nombre_curso']