from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registro

from registro import views as views_registros

#Seguridad y acceso
from users import views as views_users


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

    #Pacientes
    path('lista/', views_registro.lista_pacientes, name='lista_pacientes'),
    path('nuevo/', views_registro.crear_paciente, name='crear_paciente'),
    path('<int:id>/', views_registro.detalle_paciente, name='detalle_paciente'),
    path('<int:id>/editar/', views_registro.editar_paciente, name='editar_paciente'),
    path('<int:id>/eliminar/', views_registro.eliminar_paciente, name='eliminar_paciente'),



#Seguridad y acceso
    path('users/', views_users.user_list, name='user_list'),
    path('users/create/', views_users.user_create, name='user_create'),
    path('users/edit/<int:id>/', views_users.user_edit, name='user_edit'),
    path('users/delete/<int:id>/', views_users.user_delete, name='user_delete'),
]





