from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('login/', views.login, name="Login"),
    path('register/', views.register_user, name="register"),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('detallePaciente/', views.detallePaciente, name='detallePaciente'),
    path('medicamentos/', views_registro.recursosMedicos, name='medicamentos'),
    path('detalleMedicamento/', views.detalleMedicamento, name='detalleMedicamento'),

    #inventario
    path('inventario/', views.inventario, name='inventario'),
    path('detalleInventario/', views.detalleInventario, name='detalleInventario'),
    path('registrarInventario/', views.registrarInventario, name='registrarInventario'),
    path('editarInventario/<int:id>/', views.editarInventario, name='editarInventario'),
    #path('eliminarInventario/<int:id>/', views.eliminarInventario, name='eliminarInventario'),



    path('medicamentos_admin/', views.medicamentos, name='medicamentos_admin'),
    path('editarPaciente/', views.editarPaciente, name='editarPaciente'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarMedicamento/<int:id>/', views_registro.editar_recursoMedico, name='editarMedicamento'),
    path('registrarMedicamento/', views_registro.registrar_recursoMedico, name='registrarMedicamento'),
    path('medicamentos/eliminar/<int:id>/', views_registro.eliminar_recursoMedico, name='eliminar_emedicamento'),
]
