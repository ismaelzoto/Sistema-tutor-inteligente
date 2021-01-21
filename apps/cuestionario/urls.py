from django.conf.urls import url
from apps.cuestionario.views import cuestionarioCreate,cuestionarioList, cuestionarioDelete, cuestionarioUpdate, cuestionarioShow, search

urlpatterns = [
    url(r'^nuevo/', cuestionarioCreate.as_view(), name='cuestionariocrear'),
    url(r'^listar/', cuestionarioList.as_view(), name='cuestionariolistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', cuestionarioDelete.as_view(), name='cuestionarioeliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', cuestionarioUpdate.as_view(), name='cuestionarioeditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', cuestionarioShow.as_view(), name='cuestionariomostrar'),
    url(r'^buscar/$', search, name='cuestionariobuscar'),
]
