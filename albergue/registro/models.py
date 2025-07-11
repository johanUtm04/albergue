from django.db import models
from datetime import date

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ["-created"]

class RecursoNoMedico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de recurso")
    cantidad = models.IntegerField(default=0, verbose_name="Cantidad disponible")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Recurso No Médico"
        verbose_name_plural = "Recursos No Médicos"
        ordering = ["-created"]

class RecursoMedico(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    lote = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=[("DISP", "Disponible"), ("AGOT", "Agotado"), ("VENC", "Vencido")])
    fecha_vencimiento = models.DateField(null=True, blank=True)
    proveedor = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    @property
    def proximo_vencer(self):
        if self.fecha_vencimiento:
            return (self.fecha_vencimiento - date.today()).days
        return "Sin fecha"

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Recurso Médico"
        verbose_name_plural = "Recursos Médicos"
        ordering = ["-creado"]
        indexes = [
            models.Index(fields=['tipo', 'estado']),
        ]

class Paciente(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    diagnostico = models.TextField()
    #fecha_ingreso = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["-created"]
class Inventario(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    fecha_reabastecimiento = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
