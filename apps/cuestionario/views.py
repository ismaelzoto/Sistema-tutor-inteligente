# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import cuestionario
from apps.cuestionario.forms import CuestionarioForm
from apps.cuestionario.filters import cuestionarioFilter
from django.urls import reverse_lazy

class cuestionarioCreate(CreateView):
    model = cuestionario
    form_class = CuestionarioForm
    template_name = 'cuestionario/cuestionario_form.html'
    success_url = reverse_lazy('cuestionario:cuestionariobuscar')

class cuestionarioList(ListView):
    queryset = cuestionario.objects.order_by('id_cuestionario')
    template_name = 'cuestionario/cuestionario_list.html'
    paginate_by = 10

class cuestionarioUpdate(UpdateView):
    model = cuestionario
    form_class = CuestionarioForm
    template_name = 'cuestionario/cuestionario_form.html'
    success_url = reverse_lazy('cuestionario:cuestionariobuscar')

class cuestionarioDelete(DeleteView):
    model = cuestionario
    template_name = 'cuestionario/cuestionario_delete.html'
    success_url = reverse_lazy('cuestionario:cuestionariobuscar')

class cuestionarioShow(DetailView):
    model = cuestionario
    template_name = 'cuestionario/cuestionario_show.html'

def search(request):
    tipo_list = cuestionario.objects.all()
    tipo_filter = cuestionarioFilter(request.GET, queryset=tipo_list)
    return render(request, 'cuestionario/cuestionario_list_filter.html', {'filter': cuestionarioFilter})

