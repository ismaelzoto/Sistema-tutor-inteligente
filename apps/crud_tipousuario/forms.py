from django import forms
from apps.sistema.models import tipo_usuario

class tipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = tipo_usuario
        fields = [
            'id_tipo',
            'nombre_tipo_usuario'
        ]
        labels = {
            'id_tipo': 'Id',
            'nombre_tipo_usuario': 'Tipo de usuario'
        }

        widgets = {
            'id_tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_tipo_usuario': forms.TextInput(attrs={'class': 'form-control'}),
        }