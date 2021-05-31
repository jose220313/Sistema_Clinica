from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import PacienteForm, CitaForm
from .models import *
import random
import json

@permission_required('base.is_doctor')
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
        return redirect('VerPaciente_Doctor')
    return render(request, "doctor/paciente_form.html")

@permission_required('base.is_doctor')
def VerPaciente(request):
    viewPaciente = Paciente.objects.all()
    context = {"pacientes":viewPaciente}
    template_name = "doctor/base_list.html"
    return render(request,template_name,context)

@permission_required('base.is_doctor')
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
        return redirect('Cita_Doctor')
    return render(request, "doctor/cita_form.html", context)


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

@permission_required('base.is_doctor')
def ActualizarPaciente(request, id_paciente):
    pacientes = Paciente.objects.get(id_paciente=id_paciente)  
    idpaciente = pacientes
    
    if request.method == "GET":
        form = PacienteForm(instance=pacientes)
    else:
        form = PacienteForm(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
        return redirect("VerPaciente_Doctor") 
    return render(request, "doctor/paciente_actualizar_form.html", {"form": form,"pac":idpaciente}) 

@permission_required('base.is_doctor')
def ExpedienteView(request, id_paciente):
    '''* Modifiqué la senticia  *'''
    tipo1 = 'Quirúrgica'
    tipo2 = 'No Quirúrgica'
    expediente = Expediente.objects.filter(id_paciente=id_paciente).order_by('-id_expediente')
    quirurgico = Expediente.objects.filter(id_paciente=id_paciente,tipo_consulta=tipo1).order_by('-id_expediente')
    noQuirurgico = Expediente.objects.filter(id_paciente=id_paciente,tipo_consulta=tipo2).order_by('-id_expediente')
    
    context = {"quirurgico":quirurgico, "noQuirurgico":noQuirurgico,"general":expediente}
    template_name = 'doctor/expediente_form.html'
    return render(request,template_name, context)

@permission_required('base.is_doctor')
def ExpedienteSignosVitales(request, id_expediente):
    query = Expediente.objects.filter(id_expediente=id_expediente)
    context = {'SignosVitales':query}
    template_name = 'doctor/expediente_view.html'
    return render(request,template_name,context)

@permission_required('base.is_doctor')
def ExpedienteConsulta(request, id_expediente):
    query = Expediente.objects.filter(id_expediente=id_expediente)
    context = {'SignosVitales':query}
    template_name = 'doctor/expediente_consulta.html'
    return render(request,template_name,context)

@permission_required('base.is_doctor')
def ExpedienteUpdate(request,id_expediente):
    id="RP001"
    ex = Expediente.objects.get(id_expediente=id_expediente)
    expediente = Expediente.objects.get(id_expediente=id_expediente)
    em = Empleados.objects.get(id_empleado=id)
    if request.method == "POST":
        expediente.tipo_consulta = request.POST['tipo_consulta']
        expediente.diagnostico = request.POST['diagnostico']
        expediente.receta = request.POST['receta']
        expediente.id_empleado = em

        expediente.save()
    
    return render(request,'doctor/expediente_update.html',{"ex":ex})


class ActualizarCita(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = "doctor/cita_update.html"
    success_url = reverse_lazy("Cita_Doctor")

class BorrarCita(DeleteView):
    model = Cita
    form_class = CitaForm
    template_name = "doctor/cita_confirm_delete.html"
    success_url = reverse_lazy("Cita_Doctor")

@permission_required('base.is_doctor')
def home_doctor(request):
    return render(request, "doctor/index.html")

@permission_required('base.is_doctor')
def calendar(request):
    all_events = Cita.objects.all()
    context = {
        "citas": all_events,
    }
    return render(request, "doctor/calendar.html", context)


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
