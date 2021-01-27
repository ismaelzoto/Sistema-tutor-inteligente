# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import tipo_usuario
from apps.crud_tipousuario.forms import tipoUsuarioForm
from apps.crud_tipousuario.filters import tipo_usuarioFilter
from django.urls import reverse_lazy


class tipoCreate(CreateView):
    model = tipo_usuario
    form_class = tipoUsuarioForm
    template_name = 'tipousuario/tipousuario_form.html'
    success_url = reverse_lazy('tipousuario:tipobuscar')


class tipoList(ListView):
    queryset = tipo_usuario.objects.order_by('id_tipo')
    template_name = 'tipousuario/tipousuario_list.html'
    paginate_by = 10


class tipoUpdate(UpdateView):
    model = tipo_usuario
    form_class = tipoUsuarioForm
    template_name = 'tipousuario/tipousuario_form.html'
    success_url = reverse_lazy('tipousuario:tipobuscar')


class tipoDelete(DeleteView):
    model = tipo_usuario
    template_name = 'tipousuario/tipousuario_delete.html'
    success_url = reverse_lazy('tipousuario:tipobuscar')


class tipoShow(DetailView):
    model = tipo_usuario
    template_name = 'tipousuario/tipousuario_show.html'


def search(request):
    tipo_list = tipo_usuario.objects.all()
    tipo_filter = tipo_usuarioFilter(request.GET, queryset=tipo_list)
    return render(request, 'tipousuario/tipousuario_list_filter.html', {'filter': tipo_filter})
