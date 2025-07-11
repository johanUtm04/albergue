from django.shortcuts import render, get_object_or_404, redirect
from .models import RecursoMedico, Paciente
from .forms import RecursoMedicoForm, PacienteForm
from .models import RecursoMedico, Inventario
from .forms import RecursoMedicoForm, InventarioForm

# --- CRUD Recurso Médico ---

def recursosMedicos(request):
    medicamentos = RecursoMedico.objects.all()
    return render(request, "registro/medicamentos.html", {'medicamentos': medicamentos})

def registrar_recursoMedico(request):
    if request.method == 'POST':
        form = RecursoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamentos')
    else:
        form = RecursoMedicoForm()
    return render(request, "registro/registrarMedicamento.html", {'form': form})

def editar_recursoMedico(request, id):
    recurso = get_object_or_404(RecursoMedico, id=id)
    if request.method == 'POST':
        form = RecursoMedicoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('medicamentos')
    else:
        form = RecursoMedicoForm(instance=recurso)
    return render(request, "registro/editarMedicamento.html", {'form': form})

def eliminar_recursoMedico(request, id):
    recurso = get_object_or_404(RecursoMedico, id=id)
    if request.method == 'POST':
        recurso.delete()
        return redirect('medicamentos')
    return render(request, "registro/confirmar_eliminacion.html", {'object': recurso})


#Pacientes
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "registro/pacientes.html", {'pacientes': pacientes})


def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    return render(request, "registro/detallePaciente.html", {'paciente': paciente})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'registro/registrarPaciente.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('detalle_paciente', id=paciente.id)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'registro/editarPaciente.html', {'form': form})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')






# --- CRUD Inventario ---

def inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inicio/inventario.html', {'inventarios': inventarios})

def registrarInventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = InventarioForm()
    return render(request, 'inicio/registrarInventario.html', {'form': form})

def editarInventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('inventario')  # nombre de la url donde se lista el inventario
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inicio/editarInventario.html', {'form': form})

def eliminarInventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        inventario.delete()
        return redirect('inventario')
    return render(request, 'inicio/eliminarInventario.html', {'object': inventario})




# registro/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoRecursoNoMedico, SolicitudRecursoNoMedico
from .forms import TipoRecursoNoMedicoForm, SolicitudRecursoNoMedicoForm

def lista_tipos(request):
    tipos = TipoRecursoNoMedico.objects.all()
    return render(request, 'registro/tipos.html', {'tipos': tipos})

def registrar_tipo(request):
    form = TipoRecursoNoMedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tipos')
    return render(request, 'registro/registrar_tipo.html', {'form': form})

def lista_solicitudes(request):
    solicitudes = SolicitudRecursoNoMedico.objects.all()
    estado = request.GET.get('estado')
    if estado:
        solicitudes = solicitudes.filter(estado=estado)
    return render(request, 'registro/solicitudes.html', {'solicitudes': solicitudes})

def registrar_solicitud(request):
    form = SolicitudRecursoNoMedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_solicitudes')
    return render(request, 'registro/registrar_solicitud.html', {'form': form})
