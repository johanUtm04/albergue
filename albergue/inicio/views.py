from django.shortcuts import render

# Create your views here.

def principal (request):
    return render(request, "inicio/principal.html")

def login(request):
    return render(request, "inicio/login.html")

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        fecha_nacimiento = request.POST['fecha_nacimiento']

        if User.objects.filter(username=username).exists():
            return render(request, 'inicio/register.html', {'error': 'El nombre de usuario ya existe'})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('Login')

    # este return es obligatorio para cuando entras con GET
    return render(request, 'inicio/register.html')

def pacientes(request):
    return render(request, 'inicio/pacientes.html')

def medicamentos(request):
    return render(request, 'inicio/medicamentos.html')

def inventario(request):
    return render(request, 'inicio/inventario.html')

def detalleInventario(request):
    return render (request, 'inicio/detalleInventario.html')

def detallePaciente(request):
    return render(request, 'inicio/detallePaciente.html')

def medicamentos_admin(request):
    return render(request, 'inicio/medicamentos_admin.html')

def detalleMedicamento(request):
    return render (request, 'inicio/detalleMedicamento.html')

def editarPaciente(request):
    return render (request, 'inicio/editarPaciente.html')

def registrarPaciente(request):
    return render (request, 'inicio/registrarPaciente.html')

def editarMedicamento(request):
    return render (request, 'inicio/editarMedicamento.html')

def registrarMedicamento(request):
    return render (request, 'inicio/registrarMedicamento.html')