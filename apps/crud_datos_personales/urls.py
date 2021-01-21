
from django.conf.urls import url
from apps.crud_datos_personales.views import datospersonalesCreate, datospersonalesList, datospersonalesDelete, datospersonalesUpdate, datospersonalesShow, search

urlpatterns = [
    url(r'^nuevo/', datospersonalesCreate.as_view(), name='datospersonales_crear'),
    url(r'^listar/',datospersonalesList.as_view(),name='datospersonales_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', datospersonalesDelete.as_view(), name='datospersonales_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', datospersonalesUpdate.as_view(), name='datospersonales_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', datospersonalesShow.as_view(), name='datospersonales_mostrar'),
    url(r'^buscar/$', search, name='datospersonales_buscar'),

            ]