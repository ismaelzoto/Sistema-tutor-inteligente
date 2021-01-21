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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf.urls import include, url
from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView, RegistroNuevo, TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^tipousuarios/', include(('apps.crud_tipousuario.urls', 'apps',), namespace='tipousuario')),
    url(r'^usuarios/', include(('apps.crud_datos_personales.urls', 'apps',), namespace='usuario')),
    url(r'^datosusuarios/', include(('apps.crud_datos_cuenta.urls', 'apps',), namespace='datosusuario')),
    url(r'^inteligencias/', include(('apps.crud_inteligencias.urls', 'apps',), namespace='inteligencias')),
    url(r'^cursos/', include(('apps.crud_curso.urls', 'apps',), namespace='cursos')),
    url(r'^temascursos/', include(('apps.crud_temas_curso.urls', 'apps',), namespace='temascursos')),
    url(r'^ejercicios/', include(('apps.crud_ejercicios.urls', 'apps',), namespace='ejercicios')),
    url(r'^cuestionario/', include(('apps.cuestionario.urls', 'apps',), namespace='cuestionario')),
    url(r'^distractorespregunta/', include(('apps.crud_distractores_preguntas.urls', 'apps',), namespace='distractorespregunta')),
    url(r'^preguntas/', include(('apps.crud_preguntas_test_inteligencia.urls', 'apps',), namespace='preguntastest')),

    #url(r'^admin/', admin.site.urls),
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^iniciar-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    url(r'^nuevo-registro/$', RegistroNuevo.as_view(), name='registro'),

    url(r'^recuperar/contraseña/$', auth_views.PasswordResetView.as_view(
            template_name='registros/password_reset_form.html',
            html_email_template_name='registros/password_reset_email.html'
    ),      name='password_reset'),

    url(r'^recuperar/contraseña/hecho/$', auth_views.PasswordResetDoneView.as_view(
            template_name='registros/password_reset_done.html'
    ),      name='password_reset_done'),

    url(r'^recuperar/contraseña/(?P<uidb64>[0-9A-Za-z_\-]+)/'r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('password_reset_complete'),
            post_reset_login=True,
            template_name='registros/password_reset_confirm.html',
            post_reset_login_backend=('django.contrib.auth.backends.AllowAllUsersModelBackend'
                                      )),    name='password_reset_confirm'),

    url(r'^recuperar/contraseña/completo/$', auth_views.PasswordResetCompleteView.as_view(
            template_name='registros/password_reset_complete.html'
    ),      name='password_reset_complete'),


    url(r'^actualizar_contraseña/$', auth_views.PasswordChangeView.as_view(
        template_name='registros/password_change_form.html',
        success_url=reverse_lazy('password_change_done')),
        name='password_change'),

    url(r'^actualizar_contraseña_hecho/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='registros/password_change_done.html'),
        name='password_change_done'),

    url(r'^email_change/$', login_required(TemplateView.as_view(template_name='registros/email_change_form.html')),
        name='email_change')

    ]
