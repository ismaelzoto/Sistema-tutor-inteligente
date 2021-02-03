from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from apps.sistema.models import datos_cuenta
#from perfiles.models import Perfil
#from perfiles.forms import SignUpForm
from apps.crud_datos_cuenta.forms import datoscuentaForm
from apps.crud_datos_cuenta.filters import datoscuentaFilter
from django.urls import reverse_lazy

#...................................................
#from django.shortcuts import render, redirect
#from django.contrib.auth import logout as do_logout
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login as do_login
#......................................................


class datosusuarioCreate(CreateView):
    model = datos_cuenta
    #model = Perfil
    form_class = datoscuentaForm
    #form_class = SignUpForm
    template_name = 'datoscuenta/datoscuenta_form.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioList(ListView):
    queryset = datos_cuenta.objects.order_by('id_usuario')
    template_name = 'datoscuenta/datoscuenta_list.html'


class datosusuarioUpdate(UpdateView):
    model = datos_cuenta
    #model = Perfil
    form_class = datoscuentaForm
    #form_class = SignUpForm
    template_name = 'datoscuenta/datoscuenta_editar.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioDelete(DeleteView):
    model = datos_cuenta
    #model = Perfil
    template_name = 'datoscuenta/datoscuenta_delete.html'
    success_url = reverse_lazy('datosusuario:datosusuario_buscar')


class datosusuarioShow(DetailView):
    model = datos_cuenta
    #model = Perfil
    template_name = 'datoscuenta/datoscuenta_show.html'


def search(request):
    datoscuenta_list = datos_cuenta.objects.all()
    datoscuenta_filter = datoscuentaFilter(request.GET, queryset=datoscuenta_list)
    return render(request, 'datoscuenta/datoscuenta_list_filter.html', {'filter': datoscuenta_filter})

# .................................................................................................................................

"""def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    return render(request, "datoscuenta/welcome.html")

def register(request):
    return render(request, "datoscuenta/register.html")

def login(request):
    return render(request, "datoscuenta/login.html")

def logout(request):
    # Redireccionamos a la portada
    return redirect('/')

# ...

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "datoscuenta/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

# ...

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "datoscuenta/login.html", {'form': form})

# ...

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "datoscuenta/register.html", {'form': form})

# Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

# Si llegamos al final renderizamos el formulario
    return render(request, "datoscuenta/register.html", {'form': form})"""