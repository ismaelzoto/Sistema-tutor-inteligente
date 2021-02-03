from django import forms
from apps.sistema.models import curso


class cursoForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = [
            'id_curso',
            'nombre_curso',
            'nivel',
            'image'
        ]
        labels = {
            'idcurso': 'Id Curso',
            'nombre_curso' : 'Nombre de curso',
            'nivel' : 'Nivel',
            'image' :'Agregar imagen'
        }

