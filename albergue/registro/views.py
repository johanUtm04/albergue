from django.shortcuts import render, get_object_or_404, redirect
from .models import RecursoMedico, Paciente
from .forms import RecursoMedicoForm, PacienteForm

# LISTAR
def recursosMedicos(request):
    medicamentos = RecursoMedico.objects.all()
    return render(request, "registro/medicamentos.html", {'medicamentos': medicamentos})

# REGISTRAR
def registrar_recursoMedico(request):
    if request.method == 'POST':
        form = RecursoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamentos')
    else:
        form = RecursoMedicoForm()
    return render(request, "registro/registrarMedicamento.html", {'form': form})

# EDITAR
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

# ELIMINAR
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






