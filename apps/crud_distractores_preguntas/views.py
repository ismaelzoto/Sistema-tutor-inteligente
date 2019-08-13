from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import distractores_pregunta
from apps.crud_distractores_preguntas.forms import distractorespreguntaForm
from apps.crud_distractores_preguntas.filters import distractorespreguntaFilter
from django.urls import reverse_lazy

class distractorespreguntaCreate(CreateView):
    model = distractores_pregunta
    form_class = distractorespreguntaForm
    template_name = 'distractorespregunta/distractorespregunta_form.html'
    success_url = reverse_lazy('distractorespregunta:distractorespreguntabuscar')

class distractorespreguntaList(ListView):
    queryset = distractores_pregunta.objects.order_by('id_distractor')
    template_name = 'distractorespregunta/distractorespregunta_list.html'
    paginate_by = 10

class distractorespreguntaUpdate(UpdateView):
    model = distractores_pregunta
    form_class = distractorespreguntaForm
    template_name = 'distractorespregunta/distractorespregunta_form.html'
    success_url = reverse_lazy('distractorespregunta:distractorespreguntabuscar')

class distractorespreguntaDelete(DeleteView):
    model = distractores_pregunta
    template_name = 'distractorespregunta/distractorespregunta_delete.html'
    success_url = reverse_lazy('distractorespregunta:distractorespreguntabuscar')

class distractorespreguntaShow(DetailView):
    model = distractores_pregunta
    template_name = 'distractorespregunta/distractorespregunta_show.html'

def searchdistractorespregunta(request):
    distractorespregunta_list = distractores_pregunta.objects.all()
    distractorespregunta_filter = distractorespreguntaFilter(request.GET, queryset=distractorespregunta_list)
    return render(request, 'distractorespregunta/distractorespregunta_list_filter.html', {'filter': distractorespregunta_filter})
