from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('login/', views.login, name="Login"), # Nueva URL para el login
    path('register/', views.register_user, name = "register"),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path('detallePaciente/', views.detallePaciente, name='detallePaciente'),
    path('medicamentos_admin/', views.medicamentos_admin, name='medicamentos_admin'),
    path('detalleMedicamento/', views.detalleMedicamento, name='detalleMedicamento'),
    path('editarPaciente/', views.editarPaciente, name='editarPaciente'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarMedicamento/', views.editarMedicamento, name='editarMedicamento'),
    path('registrarMedicamento/', views.registrarMedicamento, name='registrarMedicamento'),


    path('recursos/', views_registros.lista_recursos, name='Lista_recursos'),
    path('recursos/agregar/', views_registros.agregar_recurso, name='agregar_recurso'),
]
