from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            return redirect('pacientes')
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
    return render(request, 'inicio/inventario.html')

@login_required(login_url='Login')
def detalleInventario(request):
    return render(request, 'inicio/detalleInventario.html')

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
