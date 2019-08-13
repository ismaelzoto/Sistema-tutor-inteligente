from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import inteligencias
from apps.crud_inteligencias.forms import inteligenciasForm
from apps.crud_inteligencias.filters import inteligenciasFilter
from django.urls import reverse_lazy

class inteligenciasCreate(CreateView):
    model = inteligencias
    form_class = inteligenciasForm
    template_name = 'inteligencias/inteligencias_form.html'
    success_url = reverse_lazy('inteligencias:inteligencia_buscar')

class inteligenciasList(ListView):
    queryset = inteligencias.objects.order_by('id_inteligencias')
    template_name = 'inteligencias/inteligencias_list.html'
    paginate_by = 100

class inteligenciasUpdate(UpdateView):
    model = inteligencias
    form_class = inteligenciasForm
    template_name = 'inteligencias/inteligencias_form.html'
    success_url = reverse_lazy('inteligencias:inteligencia_buscar')

class inteligenciasDelete(DeleteView):
    model = inteligencias
    template_name = 'inteligencias/inteligencias_delete.html'
    success_url = reverse_lazy('inteligencias:inteligencia_buscar')


class inteligenciaShow(DetailView):
    model = inteligencias
    template_name = 'inteligencias/inteligencias_show.html'

def searchinteligencias(request):
    inteligencias_list = inteligencias.objects.all()
    inteligencias_filter = inteligenciasFilter(request.GET, queryset=inteligencias_list)
    return render(request, 'inteligencias/inteligencias_list_filter.html', {'filter': inteligencias_filter})

