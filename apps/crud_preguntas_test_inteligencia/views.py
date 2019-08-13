from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import preguntas_test_inteligencia
from apps.crud_preguntas_test_inteligencia.forms import preguntas_test_inteligenciaForm
from apps.crud_preguntas_test_inteligencia.filters import preguntas_test_inteligenciaFilter
from django.urls import reverse_lazy

class preguntas_test_inteligenciaCreate(CreateView):
    model = preguntas_test_inteligencia
    form_class = preguntas_test_inteligenciaForm
    template_name = 'preguntas/preguntas_form.html'
    success_url = reverse_lazy('preguntastest:preguntasbuscar')

class preguntas_test_inteligenciaList(ListView):
    queryset = preguntas_test_inteligencia.objects.order_by('id_ejercicio')
    template_name = 'preguntas/preguntas_list.html'
    paginate_by = 100

class preguntas_test_inteligenciaUpdate(UpdateView):
    model = preguntas_test_inteligencia
    form_class = preguntas_test_inteligenciaForm
    template_name = 'preguntas/preguntas_form.html'
    success_url = reverse_lazy('preguntastest:preguntasbuscar')

class preguntas_test_inteligenciaDelete(DeleteView):
    model = preguntas_test_inteligencia
    template_name = 'preguntas/preguntas_delete.html'
    success_url = reverse_lazy('preguntastest:preguntasbuscar')

class preguntas_test_inteligenciaShow(DetailView):
    model = preguntas_test_inteligencia
    template_name = 'preguntas/preguntas_show.html'

def searchpreguntas(request):
    pregunta_list = preguntas_test_inteligencia.objects.all()
    pregunta_filter = preguntas_test_inteligenciaFilter(request.GET, queryset=pregunta_list)
    return render(request, 'preguntas/preguntas_list_filter.html', {'filter': pregunta_filter})
