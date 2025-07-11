from django.contrib import admin
from django.urls import path
from inicio import views
from registro import views as views_registro
from users import views as views_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('login/', views.login_view, name="Login"),  # si prefieres esta función
#   path('register/', views.register_user, name='register'),

    #inventario
    path('inventario/', views.inventario, name='inventario'),
    path('detalleInventario/', views.detalleInventario, name='detalleInventario'),
    path('registrarInventario/', views.registrarInventario, name='registrarInventario'),
    path('editarInventario/<int:id>/', views.editarInventario, name='editarInventario'),
    path('eliminarInventario/<int:id>/', views.eliminarInventario, name='eliminarInventario'),

    path('pacientes/', views.pacientes, name='pacientes'),
    path('detallePaciente/', views.detallePaciente, name='detallePaciente'),
    path('detalleMedicamento/', views.detalleMedicamento, name='detalleMedicamento'),

    path('medicamentos/', views_registro.recursosMedicos, name='medicamentos'),
    path('editarPaciente/', views.editarPaciente, name='editarPaciente'),
    path('registrarPaciente/', views.registrarPaciente, name='registrarPaciente'),
    path('editarMedicamento/<int:id>/', views_registro.editar_recursoMedico, name='editarMedicamento'),
    path('registrarMedicamento/', views_registro.registrar_recursoMedico, name='registrarMedicamento'),
    path('medicamentos/eliminar/<int:id>/', views_registro.eliminar_recursoMedico, name='eliminarMedicamento'),


    # Seguridad y acceso
    path('users/', views_users.user_list, name='user_list'),
    path('users/create/', views_users.user_create, name='user_create'),
    path('users/edit/<int:id>/', views_users.user_edit, name='user_edit'),
    path('users/delete/<int:id>/', views_users.user_delete, name='user_delete'),
    path('logout/', views.logout_view, name='logout'),





path('medicamentos/', views_registro.recursosMedicos, name='medicamentos'),
]



