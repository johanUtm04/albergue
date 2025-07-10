from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registro

from registro import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('login/', views.login, name="Login"), # Nueva URL para el login
    path('register/', views.register_user, name = "register"),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('detallePaciente/', views.detallePaciente, name='detallePaciente'),
    path('medicamentos/', views_registro.recursosMedicos, name='medicamentos'),
    path('detalleMedicamento/', views.detalleMedicamento, name='detalleMedicamento'),

    path('inventario/', views.inventario, name='inventario'),
    path('detalleInventario/', views.detalleInventario, name='detalleInventario'),

    path('medicamentos_admin/', views.medicamentos, name='medicamentos_admin'),
    path('editarPaciente/', views.editarPaciente, name='editarPaciente'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarMedicamento/<int:id>/', views_registro.editar_recursoMedico, name='editarMedicamento'),
    path('registrarMedicamento/', views_registro.registrar_recursoMedico, name='registrarMedicamento'),
    path('medicamentos/eliminar/<int:id>/', views_registro.eliminar_recursoMedico, name='eliminar_medicamento'),



    #path('recursos/', views_registros.lista_recursos, name='Lista_recursos'),
    #path('recursos/agregar/', views_registros.agregar_recurso, name='agregar_recurso'),
]


