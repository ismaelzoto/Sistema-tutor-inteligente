from django import forms
from apps.sistema.models import cuestionario

class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = cuestionario
        fields = [
            'id_cuestionario',
            'id_pregunta_test',
            'resultado_pregunta_cuestionario'
        ]
        labels = {
            'id_cuestionario': 'Id',
            'id_pregunta_test': 'Pregunta',
            'resultado_pregunta_cuestionario': 'Valor'
        }

        widgets = {
            'id_cuestionario': forms.TextInput(attrs={'class': 'form-control'}),
            'id_pregunta_test': forms.Select(attrs={'class': 'form-control'}),
            'resultado_pregunta_cuestionario': forms.TextInput(attrs={'class': 'form-control'}),
        }