import django_filters
from apps.sistema.models import datos_cuenta

class datoscuentaFilter(django_filters.FilterSet):
    class Meta:
        model = datos_cuenta
        fields = ['usuario']