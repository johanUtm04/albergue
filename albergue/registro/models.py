from django.db import models

# Create your models here.
from django.db import models

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
        verbose_name="Médico"
        verbose_name_plural="Médico"
        ordering=["-created"]
