from django.shortcuts import render, get_object_or_404, redirect
from .models import RecursoMedico
from .forms import RecursoMedicoForm

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
