from django.conf.urls import url
from apps.crud_tipousuario.views import tipoCreate, tipoList, tipoDelete, tipoUpdate, tipoShow, search

urlpatterns = [
    url(r'^nuevo/', tipoCreate.as_view(), name='tipocrear'),
    url(r'^listar/', tipoList.as_view(), name='tipolistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', tipoDelete.as_view(), name='tipoeliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', tipoUpdate.as_view(), name='tipoeditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', tipoShow.as_view(), name='tipomostrar'),
    url(r'^buscar/$', search, name='tipobuscar'),
]
