from django import forms
from apps.sistema.models import inteligencias

class inteligenciasForm(forms.ModelForm):
    class Meta:
        model = inteligencias
        fields = [
            'id_inteligencias',
            'tipo_de_inteligencia'
        ]
        labels = {
            'id_inteligencias':'Id Inteligencias',
            'tipo_de_inteligencia':'Tipo de Inteligencia'
        }

        widgets = {
            'id_inteligencias': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_de_inteligencia': forms.TextInput(attrs={'class':'form-control'}),
        }