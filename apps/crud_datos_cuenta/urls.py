from django.conf.urls import url
from apps.crud_datos_cuenta.views import datosusuarioCreate, datosusuarioList, datosusuarioDelete, datosusuarioUpdate, datosusuarioShow, search

urlpatterns = [
    url(r'^nuevo/', datosusuarioCreate.as_view(), name='datosusuario_crear'),
    url(r'^listar/', datosusuarioList.as_view(),name='datosusuario_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', datosusuarioDelete.as_view(), name='datosusuario_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', datosusuarioUpdate.as_view(), name='datosusuario_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', datosusuarioShow.as_view(), name='datosusuario_mostrar'),
    url(r'^buscar/$', search, name='datosusuario_buscar'),
    ]