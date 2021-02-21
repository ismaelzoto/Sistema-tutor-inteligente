from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.sistema.models import datos_personales
from apps.crud_datos_personales.forms import datospersonalesForm
from apps.crud_datos_personales.filters import datospersonalesFilter
from django.urls import reverse_lazy

class datospersonalesCreate(CreateView):
    model = datos_personales
    form_class = datospersonalesForm
    template_name = 'datospersonales/datospersonales_form.html'
    success_url = reverse_lazy('usuario:datospersonales_buscar')


class datospersonalesList(ListView):
    queryset = datos_personales.objects.order_by('nombre')
    template_name = 'datospersonales/datospersonales_list.html'


class datospersonalesUpdate(UpdateView):
    model = datos_personales
    form_class = datospersonalesForm
    template_name = 'datospersonales/datospersonales_editar.html'
    success_url = reverse_lazy('usuario:datospersonales_buscar')


class datospersonalesDelete(DeleteView):
    model = datos_personales
    template_name = 'datospersonales/datospersonales_delete.html'
    success_url = reverse_lazy('usuario:datospersonales_listar')


class datospersonalesShow(DetailView):
    model = datos_personales
    template_name = 'datospersonales/datospersonales_show.html'


def search(request):
    datospersonales_list = datos_personales.objects.all()
    datopersonales_filter = datospersonalesFilter(request.GET, queryset=datospersonales_list)
    return render(request, 'datospersonales/datospersonales_list_filter.html', {'filter': datopersonales_filter})
