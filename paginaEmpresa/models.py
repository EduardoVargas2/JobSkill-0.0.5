from django.db import models
from jobskill1.models import Empresa

# Create your models here.

class Puesto(models.Model):
    nombrePuesto=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=255)
    requisitos=models.CharField(max_length=255)
    sueldoBase=models.FloatField()
    beneficios=models.CharField(max_length=255, null=True, blank=True)
    disponibles=models.IntegerField()
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='puesto'
        verbose_name_plural='puestos'
        
    def __str__(self):
        return self.nombrePuesto
    
