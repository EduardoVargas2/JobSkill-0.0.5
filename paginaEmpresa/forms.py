from django import forms
from .models import Puesto
from .models import Empresa  



class PuestoForm(forms.ModelForm):
    class Meta:
        model=Puesto
        fields=["nombrePuesto", "descripcion", "requisitos", "sueldoBase", "beneficios", "disponibles"]
        labels = {
            'nombrePuesto': 'Nombre del Puesto',
            'descripcion': 'Descripción del Puesto',
            'requisitos': 'Requisitos para el Puesto',
            'sueldoBase': 'Sueldo Base en Pesos Mexicanos (Por Semana)',
            'beneficios': 'Beneficios Ofrecidos',
            'disponibles': 'Vacantes Disponibles'
        }
        widgets = {
            'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe la naturaleza del puesto que ofreces...'}),
            'requisitos' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe lo que necesitas, puede ser en forma de lista, ej. \n-Ser honesto\n-Ser puntual\n-Tener disponibilidad de tiempo\n-etc.'}),
            'beneficios' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Beneficios extra que tu empresa da, como prestaciones, etc.'}),
        }
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'descripcion', 'direccion', 'objetivo', 'telefono']
        
        
        
        
