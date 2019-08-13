import django_filters
from apps.sistema.models import distractores_pregunta

class distractorespreguntaFilter(django_filters.FilterSet):
    class Meta:
        model = distractores_pregunta
        fields = ['distractor']