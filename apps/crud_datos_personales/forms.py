from django import forms
from apps.sistema.models import datos_personales

class datospersonalesForm(forms.ModelForm):
    class Meta:
        model = datos_personales
        fields =[
            'id_datos',
            'nombre',
            'a_paterno',
            'a_materno',
            'edad',
            'tipo_usuario',
            'datos_cuenta'
        ]
        labels = {
            'id_datos': 'Codigo',
            'nombre': 'Nombres',
            'a_paterno':'Apellido Paterno',
            'a_materno':'Apellido Materno',
            'edad':'Edad',
            'tipo_usuario':'id de tipo',
            'datos_cuenta':'id de usuarios'
        }
        widgets = {
            'id_datos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'a_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'a_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'datos_cuenta': forms.Select(attrs={'class': 'form-control'}),
        }