from django.conf.urls import url

from apps.crud_curso.views import cursoCreate, cursoList, cursoDelete, cursoUpdate, cursoShow, searchcurso, agregarcurso


urlpatterns = [
    url(r'^nuevo/$', cursoCreate.as_view(), name='cursocrear'),
    url(r'^listar/$', cursoList.as_view(), name='cursolistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', cursoDelete.as_view(), name='cursoeliminar'),
    url(r'^editar/(?P<pk>\d+)/$', cursoUpdate.as_view(), name='cursoeditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', cursoShow.as_view(), name='cursomostrar'),
    url(r'^buscar/$', searchcurso, name='cursobuscar'),
    url(r'^agregar/(?P<pk>\d+)/$', agregarcurso.as_view(), name='cursoagregar'),

        ]
