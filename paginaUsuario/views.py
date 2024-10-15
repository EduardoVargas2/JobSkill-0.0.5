from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import solicitudForm
from paginaEmpresa.models import Puesto
from paginaUsuario.models import Solicitud
from jobskill1.models import Empresa, Usuarios
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuarios
from .forms import EditarPerfil




# Create your views here.
@login_required
def home(request): #No en funcionamiento
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/home.html")


@login_required
def perfil(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
        datos = get_object_or_404(Usuarios, user=request.user)
        
    return render(request, "paginaUsuario/perfil.html", {'datos': datos})


@login_required
def trabajos(request): #Este es el home
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    puestos=Puesto.objects.all()
    return render(request, "paginaUsuario/trabajos.html", {"puestos":puestos})


@login_required
def trabajosD(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/trabajosD.html")



def resultado(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/resultado.html")



@login_required
def postulacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    usuario=Usuarios.objects.get(user=request.user)
    if request.method=="POST":
        solicitud=solicitudForm(request.POST, request.FILES)
        puesto=Puesto.objects.get(id=request.session.get("id"))
        empresa=Empresa.objects.get(nombre=puesto.empresa)
        if solicitud.is_valid():
            soli=solicitud.save(commit=False)
            try:
                soli.postulante=usuario
                soli.puesto=puesto
                soli.save()
                puestos=Puesto.objects.all()
                return render(request, "paginaUsuario/trabajos.html", {"puestos":puestos, "alert":True})
            except Usuarios.DoesNotExist:
                solicitud.add_error(None, "No se encontró una empresa asociada con este usuario.")
        else:
            return render(request, "paginaUsuario/postulacion.html", {"form":solicitud, "puesto":puesto, "empresa":empresa})
    id=request.GET.get("id")
    request.session["id"]=id
    if id is not None:
        try:
            id=int(id)
        except:
            return HttpResponseBadRequest("ID no es un número válido.")
    puesto=Puesto.objects.get(id=id)
    empresa=Empresa.objects.get(nombre=puesto.empresa)
    form=solicitudForm()
    request.session["puesto"]=puesto.id
    solicitud=Solicitud.objects.filter(postulante=usuario, puesto=puesto)
    return render(request, "paginaUsuario/postulacion.html", {"form":form, "puesto":puesto, "empresa":empresa, "solicitud":solicitud})


def notificacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    usuario=Usuarios.objects.get(user=request.user)
    solicitud=Solicitud.objects.filter(postulante=usuario)
    return render(request, "paginaUsuario/notificacion.html", {"solicitudes" : solicitud})


def editar_perfil(request):
    # Obtener la empresa asociada al usuario
    aspirante = get_object_or_404(Usuarios, user=request.user)

    if request.method == 'POST':
        # Si el formulario fue enviado, cargar los datos en el formulario
        form = EditarPerfil(request.POST, instance=aspirante)
        if form.is_valid():
            # Guardar los datos actualizados
            form.save()
            return redirect('perfil')  # Redirige de vuelta al perfil de la empresa
    else:
        # Si es una solicitud GET, mostrar el formulario con los datos actuales
        form = EditarPerfil(instance=aspirante)

    return render(request, 'paginaUsuario/editar_perfil.html', {'form': form})