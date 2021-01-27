from django import forms
from apps.sistema.models import preguntas_test_inteligencia


class preguntas_test_inteligenciaForm(forms.ModelForm):
    class Meta:
        model = preguntas_test_inteligencia
        fields = [
            'id_pregunta_test',
            'num_pregunta',
            'pregunta',
            'inteligencias'
        ]
        labels = {
            'id_pregunta_test': 'ID',
            'num_pregunta':'Número de pregunta',
            'pregunta':'Pregunta',
            'inteligencias': 'Inteligencias'
        }

        widgets = {
            'id_pregunta_test': forms.TextInput(attrs={'class': 'form-control'}),
            'num_pregunta': forms.TextInput(attrs={'class': 'form-control'}),
            'pregunta': forms.TextInput(attrs={'class': 'form-control'}),
            'inteligencias': forms.Select(attrs={}),
        }