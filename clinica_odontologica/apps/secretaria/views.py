from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import PacienteForm, CitaForm, ExpedienteForm
from .models import *
import random
import json

@permission_required('base.is_secretary')
def CrearPaciente(request):

    if request.method == "POST":
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        direccion = request.POST["direccion"]
        correo_electronico = request.POST["correo_electronico"]
        peso = request.POST["peso"]
        pulso = request.POST["pulso"]
        temperatura = request.POST["temperatura"]
        presion_arterial = request.POST["presion_arterial"]
        enfermedades = request.POST["enfermedades"]
        alergias = request.POST["alergias"]
        medicamentos = request.POST["medicamentos"]
        nombre_medico = request.POST["nombre_medico"]
        telefono_medico = request.POST["telefono_medico"]
        persona_refiere = request.POST["persona_refiere"]
        cod = generar_codigo(nombres, apellidos)
        
        Paciente.objects.create(
            id_paciente=cod,
            nombres=nombres,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            genero=genero,
            telefono=telefono,
            direccion=direccion,
            correo_electronico=correo_electronico,
        )
        Expediente.objects.create(
            peso=peso,
            pulso=pulso,
            temperatura=temperatura,
            presion_arterial=presion_arterial,
            enfermedades=enfermedades,
            alergias=alergias,
            medicamentos=medicamentos,
            nombre_medico=nombre_medico,
            telefono_medico=telefono_medico,
            persona_refiere=persona_refiere,
            id_paciente=Paciente.objects.get(id_paciente=cod),
        )
    return render(request, "secretaria/paciente_form.html")


class AgregarExpediente(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    template_name = "secretaria/expediente_form.html"
    success_url = reverse_lazy("VerPaciente")

    def get_initial(self):
        initial = super().get_initial()
        initial["id_paciente"] = self.kwargs["id_paciente"]
        return initial

@permission_required('base.is_secretary')
def VerPaciente(request):
    viewPaciente = Paciente.objects.all()
    context = {"pacientes":viewPaciente}
    template_name = "secretaria/base_list.html"
    return render(request,template_name,context)

@permission_required('base.is_secretary')
def CrearCita(request):
    paciente = Paciente.objects.all()
    empleado = Empleados.objects.all()
    cita = Cita.objects.all().order_by('-fecha')
    context = {"Pacientes": paciente, "Empleados":empleado,"Cita":cita}

    if request.method == "POST":
        nombre = request.POST["nombres"]
        apellido = request.POST["apellidos"]
        telefono = request.POST["telefono"]
        motivo = request.POST["motivo_consulta"]
        fecha = request.POST["fecha"]
        hora = request.POST["hora"]
        id_empleado = request.POST["id_empleado"]
        cita = Cita.objects.create(
            nombres=nombre,
            apellidos=apellido,
            telefono=telefono,
            motivo_consulta=motivo,
            fecha=fecha,
            hora=hora,
            id_empleado=Empleados.objects.get(id_empleado=id_empleado)
        )
        return redirect('Cita')
    return render(request, "secretaria/cita_form.html", context)


def buscar(request):
    id_paciente = request.GET.get("id_paciente")
    codigo = respuesta(id_paciente)
    pacientes = Paciente.objects.filter(id_paciente=codigo)
    pacientes = [paciente_serializer(paciente) for paciente in pacientes]
    return HttpResponse(json.dumps(pacientes), content_type="application/json")


def paciente_serializer(p):
    return {"nombres": p.nombres, "apellidos": p.apellidos, "telefono": p.telefono}


def respuesta(id_paciente):
    temp = id_paciente.split(" ")
    return temp[0]

@permission_required('base.is_secretary')
def ActualizarPaciente(request, id_paciente):
    pacientes = Paciente.objects.get(id_paciente=id_paciente)  
    idpaciente = pacientes
    
    if request.method == "GET":
        form = PacienteForm(instance=pacientes)
    else:
        form = PacienteForm(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
        return redirect("VerPaciente") 
    return render(request, "secretaria/paciente_actualizar_form.html", {"form": form,"pac":idpaciente}) 
    
@permission_required('base.is_secretary')
def ExpedienteView(request, id_paciente):
    query = Expediente.objects.filter(id_paciente=id_paciente)
    expedientes = query
    context = {"expedientes":expedientes}
    template_name = 'secretaria/paciente_detail.html'
    return render(request,template_name, context)

class ActualizarCita(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = "secretaria/cita_update.html"
    success_url = reverse_lazy("Cita")


class BorrarCita(DeleteView):
    model = Cita
    form_class = CitaForm
    template_name = "secretaria/cita_confirm_delete.html"
    success_url = reverse_lazy("Cita")


@permission_required('base.is_secretary')
def home_secretary(request):
    return render(request, "secretaria/index.html")

@permission_required('base.is_secretary')
def calendar(request):
    all_events = Cita.objects.all()
    context = {
        "citas": all_events,
    }
    return render(request, "secretaria/calendar.html", context)


def generar_codigo(nombre, apellido):

    nombreCompleto = nombre + " " + apellido

    temp = nombreCompleto.split(" ")
    codigoNombre = ""

    # GENERA UN CODIGO CON EL NOMBRE
    for contador in temp:
        codigoNombre += contador[0]

    # GENERAR CODIGO COMPLETO
    for contador2 in range(0, 2):
        convertirNumero = random.randint(1, 101)
        numero = str(convertirNumero)
        codigoNombre = codigoNombre + "" + numero

    return codigoNombre
    
def validarCita(request):
    id_empleado = request.POST.get("id_empleado")
    fecha = request.POST.get("fecha")
    hora = request.POST.get("hora")
    validarFecha = Cita.objects.filter(id_empleado=id_empleado, fecha=fecha,hora=hora)
    if validarFecha:
        validarFecha = 'La fecha ya existe'
        return HttpResponse(json.dumps(validarFecha),  content_type="application/json")
