from django import forms
from apps.sistema.models import distractores_pregunta

class distractorespreguntaForm(forms.ModelForm):
    class Meta:
        model = distractores_pregunta
        fields = [
            'id_distractor',
            'distractor',
            'id_ejercicio'
        ]
        labels = {
            'id_distractor': 'ID distractor',
            'distractor': 'Nombre del distractor',
            'id_ejercicio': 'Ejercicio'
        }
        widgets = {
            'id_distractor': forms.TextInput (attrs={'class':'form-control'}),
            'distractor': forms.TextInput (attrs={'class':'form-control'}),
            'id_ejercicio': forms.Select(attrs={'class': 'form-control'}),
        }