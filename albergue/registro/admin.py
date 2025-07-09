from django.contrib import admin
from .models import Medico


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'especialidad', 'telefono')
    search_fields = ('nombre', 'apellido', 'especialidad', 'telefono')
    list_filter = ('especialidad',)
    ordering = ('apellido', 'nombre')  # Ordena primero por apellido, luego por nombre
admin.site.register(Medico,MedicoAdmin)