from django.urls import path
from paginaEmpresa.views import *
from . import views


urlpatterns=[
    path('', home, name="homeE"),
    path('agregar/', agregar, name="agregar"),
    path('perfil/', perfil, name="perfil"),
    path('solicitud/', solicitud, name="solicitud"),
    path('candidato/', postulante, name="candidato"),
    path('editar_perfil_empresa/', editar_perfil_empresa, name="editar_perfil_empresa"),
    path('editar/<int:puesto_id>/', editar_puesto, name='editar_puesto'),

    
]
