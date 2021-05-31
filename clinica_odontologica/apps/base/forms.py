from .models import Paciente, Cita,Expediente
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from random import sample

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['id_paciente', 'nombres', 'apellidos', 'fecha_nacimiento', 'genero', 'telefono', 'direccion', 'correo_electronico']

        widgets = {
            'id_paciente':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'nombres':forms.TextInput(attrs={'class':'validate', 'type':'text','id':'nombres','name':'nombres'}),
            'apellidos':forms.TextInput(attrs={'class':'validate', 'type':'text','id':'apellidos','name':'apellidos'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'datepicker', 'type':'text'}),
            'genero':forms.Select(attrs={'type':'text'}), 
            'telefono':forms.TextInput(attrs={'class':'validate', 'type':'text','id':'telefono','name':'telefono'}),
            'direccion':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'correo_electronico':forms.TextInput(attrs={'class':'validate', 'type':'text'})
        }

      
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['id_cita','nombres','apellidos','telefono','motivo_consulta','fecha','hora','id_empleado']
        
        widgets = {
            'id_cita':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'nombres':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'apellidos':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'telefono':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'motivo_consulta':forms.TextInput(attrs={'class':'validate', 'type':'text'}),
            'fecha':forms.DateInput(attrs={'class':'datepicker', 'type':'text'}),
            'hora':forms.TimeInput(attrs={'class':'timepicker', 'type':'time','min':'06:00','max':'19:00','step':'3600'}),
            'id_empleado':forms.Select(attrs={'type':'text'})
        }

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['tipo_consulta','diagnostico']

        widgets = {
            'diagnostico':forms.Textarea(attrs={'id':'diagnostico', 'class':'materialize-textarea','data-length':'120'}),
            'tipo_consulta':forms.Select(attrs={'type':'text','id':'tipo_consulta'})
        }