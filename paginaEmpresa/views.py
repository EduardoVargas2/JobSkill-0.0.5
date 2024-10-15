from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PuestoForm
from .models import Puesto
from jobskill1.models import Empresa
from paginaUsuario.models import Solicitud
from .forms import EmpresaForm
from django.contrib.auth.decorators import login_required






# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.usuario==True:
            return redirect("homeU")
    empresa=Empresa.objects.get(user=request.user)
    puestos=Puesto.objects.filter(empresa=empresa)
    return render(request, "paginaEmpresa/editar.html", {"puestos":puestos})

@login_required
def agregar(request):
    if request.user.is_authenticated:
        if request.user.usuario==True:
            return redirect("homeU")
    if request.method=="POST":
        form=PuestoForm(request.POST)
        if form.is_valid():
            puesto=form.save(commit=False)
            try:
                empresa=Empresa.objects.get(user=request.user)
                puesto.empresa=empresa
                puesto.save()
                return redirect("homeE")
            except Empresa.DoesNotExist:
                form.add_error(None, "No se encontró una empresa asociada con este usuario.")
        else:
            return render(request, "paginaEmpresa/agregar.html", {"form":form})
    else:
        form=PuestoForm()
    return render(request, "paginaEmpresa/agregar.html", {"form":form})

@login_required
def perfil(request):
    if request.user.is_authenticated:
            if request.user.usuario==True:
                return redirect("homeU")  
    empresa = get_object_or_404(Empresa, user=request.user)
    return render(request, "paginaEmpresa/perfil.html", {'empresa': empresa})

@login_required
def solicitud(request):
    if request.user.is_authenticated:
        if request.user.usuario==True:
            return redirect("homeU")
    id=request.GET.get("id")
    request.session["id"]=id
    if id is not None:
        try:
            id=int(id)
        except:
            return HttpResponseBadRequest("ID no es un número válido.")
    solicitudes=Solicitud.objects.filter(puesto=id)
    puesto=Puesto.objects.get(id=id)
    return render(request, "paginaEmpresa/solicitud.html", {"solicitudes":solicitudes, "puesto":puesto})

@login_required
def postulante(request):
    if request.user.is_authenticated:
        if request.user.usuario==True:
            return redirect("homeU")
    if request.method=="POST":
        id=request.session.get("id")
        solicitud=Solicitud.objects.get(id=id)
        solicitud.aprobado = True  # Cambia el valor del campo a True
        solicitud.save()
        return redirect("home")
    id=request.GET.get("id")
    request.session["id"]=id
    if id is not None:
        try:
            id=int(id)
        except:
            return HttpResponseBadRequest("ID no es un número válido.")
    solicitud=Solicitud.objects.get(id=id)
    return render(request, "paginaEmpresa/postulante.html", {"solicitud":solicitud})

@login_required
def editar_perfil_empresa(request):
    empresa = get_object_or_404(Empresa, user=request.user)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige de vuelta al perfil de la empresa
    else:
        # Si es una solicitud GET, mostrar el formulario con los datos actuales
        form = EmpresaForm(instance=empresa)

    return render(request, 'paginaEmpresa/editar_perfil_empresa.html', {'form': form})
@login_required
def editar_puesto(request, puesto_id):
    puesto = get_object_or_404(Puesto, id=puesto_id)
    if request.method == 'POST':
        form = PuestoForm(request.POST, instance=puesto)
        if form.is_valid():
            form.save()
            return redirect('home')  # Cambia 'lista_puestos' por tu URL real
    else:
        form = PuestoForm(instance=puesto)
    return render(request, 'paginaEmpresa/editar_puesto.html', {'form': form})
    
   
    