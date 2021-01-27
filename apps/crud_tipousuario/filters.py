import django_filters
from apps.sistema.models import tipo_usuario


class tipo_usuarioFilter(django_filters.FilterSet):
    class Meta:
        model = tipo_usuario
        fields = ['id_tipo','nombre_tipo_usuario']