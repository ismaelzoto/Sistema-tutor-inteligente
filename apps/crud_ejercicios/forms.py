from django import forms
from apps.sistema.models import ejercicios

class ejerciciosForm(forms.ModelForm):
    class Meta:
        model = ejercicios
        fields = [
            'id_ejercicio',
            'nombre_ejercicio',
            'puntaje',
            'temas_curso'
        ]
        labels = {
            'id_ejercicio': 'ID Ejercicio',
            'nombre_ejercicio': 'Nombre del ejercicio',
            'puntaje': 'Puntaje',
            'temas_curso': 'Tema'
        }
        widgets = {
            'id_ejercicio': forms.TextInput (attrs={'class':'form-control'}),
            'nombre_ejercicio': forms.TextInput (attrs={'class':'form-control'}),
            'puntaje': forms.TextInput (attrs={'class':'form-control'}),
            'temas_curso': forms.Select(attrs={}),
        }