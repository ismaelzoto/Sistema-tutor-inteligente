from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.sistema.models import datos_cuenta
from apps.crud_datos_cuenta.forms import datoscuentaForm
from apps.crud_datos_cuenta.filters import datoscuentaFilter
from django.urls import reverse_lazy

class datosusuarioCreate(CreateView):
    model = datos_cuenta
    form_class = datoscuentaForm
    template_name = 'datoscuenta/datoscuenta_form.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioList(ListView):
    queryset = datos_cuenta.objects.order_by('id_usuario')
    template_name = 'datoscuenta/datoscuenta_list.html'


class datosusuarioUpdate(UpdateView):
    model = datos_cuenta
    form_class = datoscuentaForm
    template_name = 'datoscuenta/datoscuenta_form.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioDelete(DeleteView):
    model = datos_cuenta
    template_name = 'datoscuenta/datoscuenta_delete.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioShow(DetailView):
    model = datos_cuenta
    template_name = 'datoscuenta/datoscuenta_show.html'


def search(request):
    datoscuenta_list = datos_cuenta.objects.all()
    datoscuenta_filter = datoscuentaFilter(request.GET, queryset=datoscuenta_list)
    return render(request, 'datoscuenta/datoscuenta_list_filter.html', {'filter': datoscuenta_filter})
