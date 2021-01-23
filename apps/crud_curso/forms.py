from django import forms
from apps.sistema.models import curso


class cursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = [
            'id_curso',
            'nombre_curso',
            'nivel'
        ]
        labels = {
            'idcurso': 'Id Curso',
            'nombre_curso' : 'Nombre de curso',
            'nivel' : 'Nivel'
        }

        widgets = {
            'id_curso': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_curso': forms.TextInput(attrs={'class':'form-control'}),
            'nivel': forms.TextInput(attrs={'class':'form-control'})
        }

