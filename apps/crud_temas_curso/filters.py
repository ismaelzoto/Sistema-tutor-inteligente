import django_filters
from apps.sistema.models import temas_curso

class temas_cursoFilter(django_filters.FilterSet):
    class Meta:
        model = temas_curso
        fields = ['id_temas','nombre_temas','curso']