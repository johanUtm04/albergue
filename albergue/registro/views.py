from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import RecursoMedico
from django.contrib import messages
from django.utils import timezone

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

def agregar_recurso(request):
    if request.method == 'POST':
        try:
            # Crear el recurso con los datos del formulario
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
            render (request,'RecursosMedicos/RecursosMedicos.html')
            
        except Exception as e:
            messages.error(request, f'Error al agregar el recurso: {str(e)}')
            return render(request,'RecursosMedicos/RecursosMedicos.html')
    
    return render(request,'RecursosMedicos/AgregarRecursoMedico.html')
