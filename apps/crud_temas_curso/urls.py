from django.conf.urls import url
from apps.crud_temas_curso.views import temas_cursoCreate, temas_cursoList, temas_cursoDelete, temas_cursoUpdate, temas_cursoShow, search

urlpatterns = [
    url(r'^nuevo/', temas_cursoCreate.as_view(), name='temas_curso_crear'),
    url(r'^listar/', temas_cursoList.as_view(), name='temas_curso_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', temas_cursoDelete.as_view(), name='temas_curso_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', temas_cursoUpdate.as_view(), name='temas_curso_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', temas_cursoShow.as_view(), name='temas_curso_mostrar'),
    url(r'^buscar/$', search, name='temas_curso_buscar'),
]