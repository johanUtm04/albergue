from django import forms
from .models import Medico, RecursoMedico, RecursoNoMedico, Paciente

# Formulario para el modelo Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'  # Incluye todos los campos del modelo
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Formulario para el modelo RecursoMedico
class RecursoMedicoForm(forms.ModelForm):
    class Meta:
        model = RecursoMedico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'tipo': forms.TextInput(attrs={'class': 'form-input'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-input'}),
            'lote': forms.TextInput(attrs={'class': 'form-input'}),
            'estado': forms.Select(attrs={'class': 'form-input'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-input'}),
        }

# Formulario para el modelo RecursoNoMedico
class RecursoNoMedicoForm(forms.ModelForm):
    class Meta:
        model = RecursoNoMedico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'diagnostico']
