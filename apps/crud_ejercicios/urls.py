from django.conf.urls import url

from apps.crud_ejercicios.views import ejerciciosCreate, ejerciciosList, ejerciciosDelete, ejerciciosUpdate, ejerciciosShow, searchejercicios

urlpatterns = [
    url(r'^nuevo/', ejerciciosCreate.as_view(), name='ejercicioscrear'),
    url(r'^listar/', ejerciciosList.as_view(), name='ejercicioslistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', ejerciciosDelete.as_view(), name='ejercicioseliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', ejerciciosUpdate.as_view(), name='ejercicioseditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', ejerciciosShow.as_view(), name='ejerciciosmostrar'),
    url(r'^buscar/$', searchejercicios, name='ejerciciosbuscar'),
]