"""OpenMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^tipousuarios/', include(('apps.crud_tipousuario.urls', 'apps',), namespace='tipousuario')),
    url(r'^usuarios/', include(('apps.crud_datos_personales.urls', 'apps',), namespace='usuario')),
    url(r'^datosusuarios/', include(('apps.crud_datos_cuenta.urls', 'apps',), namespace='datosusuario')),
    url(r'^inteligencias/', include(('apps.crud_inteligencias.urls', 'apps',), namespace='inteligencias')),
    url(r'^cursos/', include(('apps.crud_curso.urls', 'apps',), namespace='cursos')),
    url(r'^temascursos/', include(('apps.crud_temas_curso.urls', 'apps',), namespace='temascursos')),
    url(r'^ejercicios/', include(('apps.crud_ejercicios.urls', 'apps',), namespace='ejercicios')),
    url(r'^distractorespregunta/', include(('apps.crud_distractores_preguntas.urls', 'apps',), namespace='distractorespregunta')),
    url(r'^preguntas/', include(('apps.crud_preguntas_test_inteligencia.urls', 'apps',), namespace='preguntastest'))
]
