from django import forms
from apps.sistema.models import datos_cuenta

class datoscuentaForm(forms.ModelForm):
    class Meta:
        model = datos_cuenta
        fields =[
            'id_usuario',
            'usuario',
            'password'
        ]
        labels = {
            'id_usuario': 'ID Usuario',
            'usuario': 'Nombre del usuario',
            'password':'Password'
        }
        widgets = {
            'id_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }