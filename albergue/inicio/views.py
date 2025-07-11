from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from registro.models import Inventario, TipoRecursoNoMedico, SolicitudRecursoNoMedico
from registro.forms import InventarioForm, TipoRecursoNoMedicoForm, SolicitudRecursoNoMedicoForm

# Vista principal
def principal(request):
    return render(request, "inicio/principal.html")

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_pacientes')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'inicio/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('Login')

# Vistas protegidas
@login_required(login_url='Login')
def pacientes(request):
    return render(request, 'inicio/pacientes.html')

@login_required(login_url='Login')
def medicamentos(request):
    return render(request, 'inicio/medicamentos.html')

@login_required(login_url='Login')
def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inicio/inventario.html', {'inventarios': inventarios})

@login_required(login_url='Login')
def detalleInventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    return render(request, 'inicio/detalleInventario.html', {'inventario': inventario})

@login_required(login_url='Login')
def editarInventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inicio/editarInventario.html', {'form': form})

@login_required(login_url='Login')
def eliminarInventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario')
    return render(request, 'inicio/eliminarInventario.html', {'object': inventario})

@login_required(login_url='Login')
def registrarInventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm()
    return render(request, 'inicio/registrarInventario.html', {'form': form})

# Vistas adicionales (puedes eliminarlas si no se usan)
@login_required(login_url='Login')
def detallePaciente(request):
    return render(request, 'inicio/detallePaciente.html')

@login_required(login_url='Login')
def medicamentos_admin(request):
    return render(request, 'inicio/medicamentos_admin.html')

@login_required(login_url='Login')
def detalleMedicamento(request):
    return render(request, 'inicio/detalleMedicamento.html')

@login_required(login_url='Login')
def editarPaciente(request):
    return render(request, 'inicio/editarPaciente.html')

@login_required(login_url='Login')
def registrarPaciente(request):
    return render(request, 'inicio/registrarPaciente.html')

@login_required(login_url='Login')
def editarMedicamento(request):
    return render(request, 'inicio/editarMedicamento.html')

@login_required(login_url='Login')
def registrarMedicamento(request):
    return render(request, 'inicio/registrarMedicamento.html')

# Tipos de Recurso No Médico
@login_required(login_url='Login')
def lista_tipos(request):
    tipos = TipoRecursoNoMedico.objects.all()
    return render(request, 'registro/tipos.html', {'tipos': tipos})

@login_required(login_url='Login')
def registrar_tipo(request):
    form = TipoRecursoNoMedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tipos')
    return render(request, 'registro/registrar_tipo.html', {'form': form})

# Solicitudes
@login_required(login_url='Login')
def lista_solicitudes(request):
    solicitudes = SolicitudRecursoNoMedico.objects.all()
    estado = request.GET.get('estado')
    if estado:
        solicitudes = solicitudes.filter(estado=estado)
    return render(request, 'registro/solicitudes.html', {'solicitudes': solicitudes})

@login_required(login_url='Login')
def registrar_solicitud(request):
    form = SolicitudRecursoNoMedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_solicitudes')
    return render(request, 'registro/registrar_solicitud.html', {'form': form})
