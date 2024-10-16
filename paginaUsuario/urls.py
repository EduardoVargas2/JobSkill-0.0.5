from django.urls import path
from paginaUsuario.views import *

urlpatterns=[
    path('perfil/', perfil, name="perfilU"),
    path('', trabajos, name="homeU"),
    path('trabajosD/', trabajosD, name="trabajosDU"),
    path('resultado/', resultado, name="resultadoU"),
    path('postulacion/', postulacion, name="postulacion"),
    path('notificacion/', notificacion, name="notificacion"),
    path('editar_perfil/',editar_perfil, name="editar_perfil"),
]