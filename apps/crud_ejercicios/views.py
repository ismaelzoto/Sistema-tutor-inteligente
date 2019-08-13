from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.sistema.models import ejercicios
from apps.crud_ejercicios.forms import ejerciciosForm
from apps.crud_ejercicios.filters import ejerciciosFilter
from django.urls import reverse_lazy

class ejerciciosCreate(CreateView):
    model = ejercicios
    form_class = ejerciciosForm
    template_name = 'ejercicios/ejercicios_form.html'
    success_url = reverse_lazy('ejercicios:ejerciciosbuscar')

class ejerciciosList(ListView):
    queryset = ejercicios.objects.order_by('id_ejercicio')
    template_name = 'ejercicios/ejercicios_list.html'
    paginate_by = 10

class ejerciciosUpdate(UpdateView):
    model = ejercicios
    form_class = ejerciciosForm
    template_name = 'ejercicios/ejercicios_form.html'
    success_url = reverse_lazy('ejercicios:ejerciciosbuscar')

class ejerciciosDelete(DeleteView):
    model = ejercicios
    template_name = 'ejercicios/ejercicios_delete.html'
    success_url = reverse_lazy('ejercicios:ejerciciosbuscar')

class ejerciciosShow(DetailView):
    model = ejercicios
    template_name = 'ejercicios/ejercicios_show.html'

def searchejercicios(request):
    ejercicios_list = ejercicios.objects.all()
    ejercicios_filter = ejerciciosFilter(request.GET, queryset=ejercicios_list)
    return render(request, 'ejercicios/ejercicios_list_filter.html', {'filter': ejercicios_filter})