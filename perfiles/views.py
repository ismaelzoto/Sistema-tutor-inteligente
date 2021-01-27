from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import requests, json
from django.views.generic import CreateView, UpdateView, TemplateView
from .models import Perfil
from .forms import SignUpForm, User, EmailChangeForm, forms
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy


class BienvenidaView(TemplateView):
    template_name = 'perfiles/bienvenida.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        key = "BUSINESS-PREMIUM-DEMO-0mn3cblhl7hhfawjvrmr0a4r"
        url = "http://api.pipl.com/search/?email={}.com&key={}".format(
            email,
            key,
        )
        response = requests.get(url, params={
                'email': email,
                'key': key,
            },
        )
        string_response = response.content.decode("utf-8")
        response_content = json.loads(string_response)

        return self.render_to_response(
            self.get_context_data(
                response_content=response_content,
            )
        )


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'perfiles/bienvenida.html'


class SignOutView(LogoutView):
    template_name = "perfiles/sesion-fin.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            '''successfully logged out'''
            messages.success(request, f'{request.user.username} se desconectó correctamente!')
        else:
            '''your error message'''
            messages.error(request, f'{request.user.username} mensaje de error')
        return super().dispatch(request, *args, **kwargs)


class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'


class ActualizarView(UpdateView):
    form_class = EmailChangeForm
    template_name = 'registros/email_change_form.html'
    success_url = reverse_lazy('cambiar_correo_hecho')


class HechoView(TemplateView):
    template_name = 'registros/email_change_done.html'


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En esta parte, si el formulario es valido se guarda lo que se obtiene de él,
        se usa authenticate para que el usuario incie sesión luego de haberse registrado y
        se redirige a index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
#       usuario = authenticate(username=usuario, password=password)
#       login(self.request, usuario)
        return redirect('/nuevo-registro/')


class RegistroNuevo(TemplateView):
    template_name = 'registros/registro_nuevo.html'


"""
class EmailChangeForm(forms.Form):
        
        #A form that lets a user change set their email while checking for a change in the 
        #e-mail.
        
        error_messages = {
            'email_mismatch': _("The two email addresses fields didn't match."),
            'not_changed': _("The email address is the same as the one already defined."),
        }

        new_email1 = forms.EmailField(
            label=_("New email address"),
            widget=forms.EmailInput,
        )

        new_email2 = forms.EmailField(
            label=_("New email address confirmation"),
            widget=forms.EmailInput,
        )

        def __init__(self, user, *args, **kwargs):
            self.user = user
            super(EmailChangeForm, self).__init__(*args, **kwargs)

        def clean_new_email1(self):
            old_email = self.user.email
            new_email1 = self.cleaned_data.get('new_email1')
            if new_email1 and old_email:
                if new_email1 == old_email:
                    raise forms.ValidationError(
                        self.error_messages['not_changed'],
                        code='not_changed',
                    )
            return new_email1

        def clean_new_email2(self):
            new_email1 = self.cleaned_data.get('new_email1')
            new_email2 = self.cleaned_data.get('new_email2')
            if new_email1 and new_email2:
                if new_email1 != new_email2:
                    raise forms.ValidationError(
                        self.error_messages['email_mismatch'],
                        code='email_mismatch',
                    )
            return new_email2

        def save(self, commit=True):
            email = self.cleaned_data["new_email1"]
            self.user.email = email
            if commit:
                self.user.save()
            return self.user

    def email_change(request):
        form = EmailChangeForm()
        if request.method == 'POST':
            form = Email_Change_Form(User, request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
                    if form.cleaned_data['email1'] == form.cleaned_data['email2']:
                        user = request.user
                        u = User.objects.get(username=user)
                        # get the proper user
                        u.email = form.cleaned_data['email1']
                        u.save()
                        return HttpResponseRedirect("/accounts/profile/")
        else:
            return render_to_response("email_change.html", {'form': form},
                                      context_instance=RequestContext(request))
"""
"""
@login_required()
def email_change(request):
        form = EmailChangeForm()
        if request.method == 'POST':
            form = EmailChangeForm(User, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/iniciar-sesion/")
        else:
            return render_to_response("registros/email_change_form.html", {'form': form},
                                      context_instance=RequestContext(request))
"""