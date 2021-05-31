from django.urls import path
from apps.doctor.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Paciente/', login_required(CrearPaciente),name='Paciente_Doctor'),
    path('VerPaciente/', login_required(VerPaciente),name='VerPaciente_Doctor'),
    path('ActualizarPaciente/<str:id_paciente>', login_required(ActualizarPaciente), name='ActualizarPaciente_Doctor'),
    path('buscar/', login_required(buscar),name='buscar_Doctor'),
    path('CrearCita/',login_required(CrearCita), name='Cita_Doctor'),
    path('ActualizarCita/<int:pk>',login_required(ActualizarCita.as_view()),name='ActualizarCita_Doctor'),
    path('BorrarCita/<int:pk>', login_required(BorrarCita.as_view()),name='BorrarCita_Doctor'),
    path('Index/',login_required(home_doctor), name='Index_Doctor'), 
    path('calendar/', calendar, name='calendar_Doctor'),
    path('ExpedienteView/<str:id_paciente>',login_required(ExpedienteView), name='ExpedienteView_Doctor'),
    path('validarCita/', login_required(validarCita),name='validarCita'),

    path('ExpedienteSignosVitales/<str:id_expediente>', login_required(ExpedienteSignosVitales),name='SignosVitales'),
    path('ExpedienteConsulta/<str:id_expediente>', login_required(ExpedienteConsulta),name='ExpedienteConsulta'),
    path('ExpedienteUpdate/<str:id_expediente>', login_required(ExpedienteUpdate),name='ExpedienteUpdate'),
   ]
