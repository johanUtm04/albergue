from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('login/', views.login, name="Login"), # Nueva URL para el login
    path('register/', views.register_user, name = "register"),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('detallePaciente/', views.detallePaciente, name='detallePaciente'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    path('detalleMedicamento/', views.detalleMedicamento, name='detalleMedicamento'),

    path('inventario/', views.inventario, name='inventario'),
    path('detalleInventario/', views.detalleInventario, name='detalleInventario'),

    path('medicamentos_admin/', views.medicamentos_admin, name='medicamentos_admin'),
    path('editarPaciente/', views.editarPaciente, name='editarPaciente'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarMedicamento/', views.editarMedicamento, name='editarMedicamento'),
    path('registrarMedicamento/', views.registrarMedicamento, name='registrarMedicamento'),


]
