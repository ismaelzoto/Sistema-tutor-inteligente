import django_filters
from apps.sistema.models import preguntas_test_inteligencia

class preguntas_test_inteligenciaFilter(django_filters.FilterSet):
    class Meta:
        model = preguntas_test_inteligencia
        fields = ['id_pregunta_test' , 'pregunta']