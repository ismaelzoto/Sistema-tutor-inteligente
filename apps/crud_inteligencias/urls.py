from django.conf.urls import url
from apps.crud_inteligencias.views import inteligenciasCreate, inteligenciasList, inteligenciasDelete, inteligenciasUpdate, inteligenciaShow, searchinteligencias

urlpatterns = [
    url(r'^nuevo/', inteligenciasCreate.as_view(), name='inteligencia_crear'),
    url(r'^listar/', inteligenciasList.as_view(), name='inteligencias_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', inteligenciasDelete.as_view(), name='inteligencia_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', inteligenciasUpdate.as_view(), name='inteligencia_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', inteligenciaShow.as_view(), name='inteligencia_mostrar'),
    url(r'^buscar/$', searchinteligencias, name='inteligencia_buscar'),
]