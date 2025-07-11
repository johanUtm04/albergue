from django.shortcuts import render, get_object_or_404, redirect
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
