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