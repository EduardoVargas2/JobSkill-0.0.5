from django import forms
from .models import Solicitud
from .models import Usuarios


class solicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields=["solicitudD", "cv"]
        labels={
            "solicitudD":"¿Por qué deberías tener este puesto?",
            "cv":"Suba aquí su Currículum Vitae",
        }
        widgets = {
            'solicitudD': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Explica tus razones...'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        
class EditarPerfil(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'direccion', 'email', 'apellido', 'apellido2', 'genero', 'fecha_nacimiento', 'telefono']