from django.conf.urls import url

from apps.crud_distractores_preguntas.views import distractorespreguntaCreate, distractorespreguntaList, distractorespreguntaDelete, distractorespreguntaUpdate, distractorespreguntaShow, searchdistractorespregunta

urlpatterns = [
    url(r'^nuevo/', distractorespreguntaCreate.as_view(), name='distractorespreguntacrear'),
    url(r'^listar/', distractorespreguntaList.as_view(), name='distractorespreguntalistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', distractorespreguntaDelete.as_view(), name='distractorespreguntaeliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', distractorespreguntaUpdate.as_view(), name='distractorespreguntaeditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', distractorespreguntaShow.as_view(), name='distractorespreguntamostrar'),
    url(r'^buscar/$', searchdistractorespregunta, name='distractorespreguntabuscar'),
]