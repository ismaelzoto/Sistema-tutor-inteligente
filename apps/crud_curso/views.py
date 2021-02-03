from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.sistema.models import curso
from apps.crud_curso.forms import cursoForm
from apps.crud_curso.filters import cursoFilter
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django_filters.views import FilterView
# Create your views here.


class cursoCreate(CreateView):
    model = curso
    form_class = cursoForm
    #fields = ['id_curso', 'nombre_curso', 'nivel', 'image']
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('cursos:cursolistar')


class cursoList(ListView):
    model = curso
    template_name = 'curso/curso_list.html'
    queryset = curso.objects.order_by('nombre_curso')
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = cursoFilter(self.request.GET, queryset=self.get_queryset())
        return context


class cursoUpdate(UpdateView):
    model = curso
    form_class = cursoForm
    template_name = 'curso/curso_editar.html'
    success_url = reverse_lazy('cursos:listar')


class cursoDelete(DeleteView):
    model = curso
    template_name = 'curso/curso_delete.html'
    success_url = reverse_lazy('cursos:cursolistar')


class cursoShow(DetailView):
    model = curso
    template_name ='curso/curso_show.html'


def searchcurso(request):
    curso_list = curso.objects.all()
    curso_filter = cursoFilter(request.GET, queryset=curso_list)
    return render(request, 'curso/curso_list_filter.html', {'filter': curso_filter})


class agregarcurso(DetailView):
    model = curso
    template_name = 'curso/curso_add.html'


