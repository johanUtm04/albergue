from django.contrib import admin
from .models import RecursoMedico
from .models import Paciente

class RecursoMedicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'tipo', 'cantidad', 'estado_colorizado',
        'fecha_vencimiento', 'proveedor'
    )
    list_filter = ('tipo', 'estado', 'proveedor')
    search_fields = ('nombre', 'proveedor')
    readonly_fields = ('creado', 'actualizado', 'proximo_vencer')
    list_editable = ('cantidad',)

    def estado_colorizado(self, obj):
        from django.utils.html import format_html
        color = {
            'DISP': 'green',
            'AGOT': 'red',
            'VENC': 'darkred'
        }.get(obj.estado, 'black')
        return format_html('<span style="color: {};">{}</span>', color, obj.get_estado_display())

    estado_colorizado.short_description = 'Estado'

admin.site.register(RecursoMedico, RecursoMedicoAdmin)

class AdministrarPaciente(admin.ModelAdmin):
    list_display =  ('id', 'nombre', 'edad','diagnostico')
    search_fields = ('id', 'nombre')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Paciente, AdministrarPaciente)