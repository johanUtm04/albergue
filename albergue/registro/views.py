from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import models

from .models import RecursoMedico
from .forms import RecursoMedicoForm


# LISTAR RECURSOS CON BÚSQUEDA Y PAGINACIÓN
def lista_recursos(request):
    query = request.GET.get('q', '')
    recursos = RecursoMedico.objects.all().order_by('-creado')

    if query:
        recursos = recursos.filter(
            models.Q(nombre__icontains=query) |
            models.Q(lote__icontains=query)
        )

    paginator = Paginator(recursos, 10)  # 10 items por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'RecursosMedicos/RecursosMedicos.html', {
        'recursos': page_obj,
        'query': query
    })


# LISTAR TODOS LOS RECURSOS (sin paginación)
def recursosMedicos(request):
    medicamentos = RecursoMedico.objects.all()
    return render(request, "registro/medicamentos.html", {'medicamentos': medicamentos})


# AGREGAR RECURSO (versión manual usando request.POST)
def agregar_recurso(request):
    if request.method == 'POST':
        try:
            recurso = RecursoMedico(
                nombre=request.POST['nombre'],
                tipo=request.POST['tipo'],
                cantidad=int(request.POST['cantidad']),
                lote=request.POST['lote'],
                estado=request.POST['estado'],
                fecha_vencimiento=request.POST['fecha_vencimiento'] or None,
                proveedor=request.POST['proveedor']
            )
            recurso.save()
            messages.success(request, 'Recurso médico agregado exitosamente!')
            return redirect('lista_recursos')  # Cambia por tu url real
        except Exception as e:
            messages.error(request, f'Error al agregar el recurso: {str(e)}')
            return render(request, 'RecursosMedicos/RecursosMedicos.html')

    return render(request, 'RecursosMedicos/AgregarRecursoMedico.html')


# REGISTRAR RECURSO (usando formulario Django)
def registrar_recursoMedico(request):
    if request.method == 'POST':
        form = RecursoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso médico agregado exitosamente!')
            return redirect('lista_recursos')  # Cambia por tu url real
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RecursoMedicoForm()
    return render(request, "registro/registrarMedicamento.html", {'form': form})


# EDITAR RECURSO
def editar_recursoMedico(request, id):
    recurso = get_object_or_404(RecursoMedico, id=id)
    if request.method == 'POST':
        form = RecursoMedicoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso médico actualizado correctamente!')
            return redirect('lista_recursos')  # Cambia por tu url real
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RecursoMedicoForm(instance=recurso)
    return render(request, "registro/editarMedicamento.html", {'form': form})


# ELIMINAR RECURSO
def eliminar_recursoMedico(request, id):
    recurso = get_object_or_404(RecursoMedico, id=id)
    if request.method == 'POST':
        recurso.delete()
        messages.success(request, 'Recurso médico eliminado correctamente.')
        return redirect('lista_recursos')  # Cambia por tu url real
    return render(request, "registro/confirmar_eliminacion.html", {'object': recurso})
