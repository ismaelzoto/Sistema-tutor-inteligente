from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import temas_curso
from apps.crud_temas_curso.forms import temas_cursoForm
from apps.crud_temas_curso.filters import temas_cursoFilter
from django.urls import reverse_lazy

class temas_cursoCreate(CreateView):
    model = temas_curso
    form_class = temas_cursoForm
    template_name = 'temascurso/temas_curso_form.html'
    success_url = reverse_lazy('temascursos:temas_curso_buscar')

class temas_cursoList(ListView):
    queryset = temas_curso.objects.order_by('id_temas')
    template_name = 'temascurso/temas_curso_list.html'
    paginate_by = 10

class temas_cursoUpdate(UpdateView):
    model = temas_curso
    form_class = temas_cursoForm
    template_name = 'temascurso/temas_curso_form.html'
    success_url = reverse_lazy('temascursos:temas_curso_buscar')

class temas_cursoDelete(DeleteView):
    model = temas_curso
    template_name = 'temascurso/temas_curso_delete.html'
    success_url = reverse_lazy('temascursos:temas_curso_buscar')


class temas_cursoShow(DetailView):
    model = temas_curso
    template_name = 'temascurso/temas_curso_show.html'

def search(request):
    temas_curso_list = temas_curso.objects.all()
    temas_curso_filter = temas_cursoFilter(request.GET, queryset=temas_curso_list)
    return render(request, 'temascurso/temas_curso_list_filter.html', {'filter': temas_curso_filter})
