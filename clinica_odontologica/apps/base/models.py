from django.db import models
from django.utils.translation import ugettext as _
from decimal import Decimal


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado')
    def __str__(self):
            return self.id_cita
    
    def get_absolute_url(self):
        return reverse('id', kwargs={'pk':self.pk})

    class Meta:
        managed = False
        db_table = 'cita'


class Empleados(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=8)
    nombres_empleado = models.CharField(max_length=50)
    apellidos_empleado = models.CharField(max_length=50)
    correo_electronico = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
            return self.nombres_empleado
    
    def get_absolute_url(self):
        return reverse('id', kwargs={'pk':self.pk})

    class Meta:
        managed = False
        db_table = 'empleados'
        permissions=(
        ('is_surgeon',_('Is_Surgeon')),
        ('is_secretary',_('Is_Secretary')),
        ('is_doctor',_('Is_Doctor')),
        )
        
    def has_perm(self, perm, obj=None):
        try:
            user_perm = self.user_permissions.get(codename=perm)
        except ObjectDoesNotExist:
            user_perm = False
        if user_perm:
            return True
        else:
            return False
        

tipoCita_Select= [('Quirurgica','Quirurgica'),('No Quirurgica','No Quirurgica')]
class Expediente(models.Model):
    id_expediente = models.IntegerField(primary_key=True)
    peso = models.CharField(max_length=5, blank=False, null=False)
    pulso = models.IntegerField(default=0, blank=False, null=False)
    temperatura = models.CharField(max_length=4, blank=False, null=False)
    presion_arterial = models.IntegerField(default=0,blank=False, null=False)
    enfermedades = models.CharField(max_length=100, blank=True, null=True)
    alergias = models.CharField(max_length=50, blank=True, null=True)
    medicamentos = models.CharField(max_length=100, blank=True, null=True)
    nombre_medico = models.CharField(max_length=50, blank=True, null=True)
    telefono_medico = models.CharField(max_length=15, blank=True, null=True)
    persona_refiere = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)
    fecha_hora = models.DateTimeField()
    tipo_consulta = models.CharField(max_length=50, blank=False, null=False,choices=tipoCita_Select)
    diagnostico = models.CharField(max_length=300, blank=False, null=False)
    receta = models.CharField(max_length=300, blank=True, null=True)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, db_column='id_paciente')
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado',blank=False, null=False)
    def __str__(self):
            return self.id_expediente
    
    def get_absolute_url(self):
        return reverse('id', kwargs={'pk':self.pk})

    class Meta:
        managed = False
        db_table = 'expediente'

tipoGenero_Select= [('Masculino','Masculino'),('Femenino','Femenino')]
class Paciente(models.Model):
    id_paciente = models.CharField(primary_key=True, max_length=8)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20, choices=tipoGenero_Select)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
            return self.id_paciente
    
    def get_absolute_url(self):
        return reverse('id', kwargs={'pk':self.pk})

    class Meta:
        managed = False
        db_table = 'paciente'


class Receta(models.Model):
    id_receta = models.IntegerField(primary_key=True)
    medicamento = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=100)
    id_paciente = models.IntegerField()
    id_consulta = models.CharField(max_length=8)
    def __str__(self):
            return self.id_recete
    
    def get_absolute_url(self):
        return reverse('id', kwargs={'pk':self.pk})

    class Meta:
        managed = False
        db_table = 'receta'
