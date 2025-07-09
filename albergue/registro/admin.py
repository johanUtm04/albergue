from django.contrib import admin
from django.utils.html import format_html
from .models import Medico
from .models import RecursoNoMedico
from .models import RecursoMedico


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'telefono', 'email', 'created')
    list_filter = ('especialidad',)
    search_fields = ('nombre', 'apellido', 'especialidad', 'telefono', 'email')
    list_editable = ('telefono', 'email')
    readonly_fields = ('created', 'updated')
    ordering = ('-created',) 
admin.site.register(Medico,MedicoAdmin)


class RecursoNoMedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad','created')
    list_filter = ('tipo',)
    search_fields = ('nombre',)
    ordering = ('-created',)
    list_editable = ('cantidad',)
    readonly_fields = ('created',)
admin.site.register(RecursoNoMedico,RecursoNoMedicoAdmin)


class RecursoMedicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 
        'tipo', 
        'cantidad', 
        'lote', 
        'estado_colorizado',
        'fecha_vencimiento',
        'proveedor'
    )
    list_filter = ('tipo', 'estado', 'proveedor')
    search_fields = ('nombre', 'lote', 'proveedor')
    list_editable = ('cantidad',)
    readonly_fields = ('creado', 'actualizado', 'proximo_vencer')
    date_hierarchy = 'fecha_vencimiento'
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'tipo', 'cantidad', 'lote')
        }),
        ('Caducidad y Proveedor', {
            'fields': ('fecha_vencimiento', 'proveedor', 'proximo_vencer')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Metadatos', {
            'fields': ('creado', 'actualizado'),
            'classes': ('collapse',)
        }),
    )

    def estado_colorizado(self, obj):
        color = {
            'DISP': 'green',
            'AGOT': 'red',
            'VENC': 'darkred'
        }.get(obj.estado, 'black')
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            obj.get_estado_display()
        )
    estado_colorizado.short_description = 'Estado'
admin.site.register(RecursoMedico,RecursoMedicoAdmin)
