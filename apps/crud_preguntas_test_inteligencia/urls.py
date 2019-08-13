from django.conf.urls import url

from apps.crud_preguntas_test_inteligencia.views import preguntas_test_inteligenciaCreate, preguntas_test_inteligenciaList, preguntas_test_inteligenciaDelete, preguntas_test_inteligenciaUpdate, preguntas_test_inteligenciaShow, searchpreguntas

urlpatterns = [
    url(r'^nuevo/', preguntas_test_inteligenciaCreate.as_view(), name='preguntascrear'),
    url(r'^listar/', preguntas_test_inteligenciaList.as_view(), name='preguntaslistar'),
    url(r'^eliminar/(?P<pk>\d+)/$', preguntas_test_inteligenciaDelete.as_view(), name='preguntaseliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', preguntas_test_inteligenciaUpdate.as_view(), name='preguntaseditar'),
    url(r'^mostrar/(?P<pk>\d+)/$', preguntas_test_inteligenciaShow.as_view(), name='preguntasmostrar'),
    url(r'^buscar/$', searchpreguntas, name='preguntasbuscar'),
]