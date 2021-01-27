from django import forms
from apps.sistema.models import temas_curso


class temas_cursoForm(forms.ModelForm):
    class Meta:
        model = temas_curso
        fields = [
        'id_temas',
        'nombre_temas',
        'curso'
        ]

        labels = {
            'id_temas':'Id Temas',
            'nombre_temas':'Nombre del tema',
            'curso':'Curso'
        }

        widgets = {
            'id_temas': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_temas': forms.TextInput(attrs={'class':'form-control'}),
            'curso': forms.Select(attrs={}),
        }