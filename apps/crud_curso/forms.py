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
            'idcurso': 'ID del curso',
            'nombre_curso' : 'Nombre del curso',
            'nivel' : 'Nombre del nivel'
        }

        widgest = {
            'id_curso': forms.TextInput (attrs={'class':'form-control'}),
            'nombre_curso' : forms.TextInput(attrs={'class':'form-control'}),
            'nivel': forms.TextInput(attrs={'class':'form-control'})
        }

