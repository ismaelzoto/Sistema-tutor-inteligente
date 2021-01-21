from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView, TemplateView
from apps.sistema.models import curso
from apps.crud_curso.forms import cursoForm
from apps.crud_curso.filters import cursoFilter
from django.urls import reverse_lazy
# Create your views here.


class agregarcurso(DetailView):
    model = curso
    template_name = 'curso/curso_add.html'


class cursoCreate(CreateView):
    model = curso
    form_class = cursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('cursos:cursobuscar')


class cursoList(ListView):
    queryset = curso.objects.order_by('nombre_curso')
    template_name = 'curso/curso_list.html'
    form_class = cursoForm
    paginate_by = 2


class cursoUpdate(UpdateView):
    model = curso
    form_class = cursoForm
    template_name = 'curso/curso_editar.html'
    success_url = reverse_lazy('cursos:cursobuscar')


class cursoDelete(DeleteView):
    model = curso
    template_name = 'curso/curso_delete.html'
    success_url = reverse_lazy('cursos:cursobuscar')


class cursoShow(DetailView):
    model = curso
    template_name ='curso/curso_show.html'


def searchcurso(request):
    curso_list = curso.objects.all()
    curso_filter = cursoFilter(request.GET, queryset=curso_list)
    return render(request, 'curso/curso_list_filter.html', {'filter': curso_filter})


