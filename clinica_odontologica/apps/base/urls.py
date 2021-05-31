from django.urls import path
from apps.base.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
    
    path('Paciente/', login_required(CrearPaciente),name='Paciente_Cirujano'),
    path('VerPaciente/', login_required(VerPaciente),name='VerPaciente_Cirujano'),
    path('ActualizarPaciente/<str:id_paciente>', login_required(ActualizarPaciente), name='ActualizarPaciente_Cirujano'),
    path('buscar/', login_required(buscar),name='buscar_Cirujano'),
    path('CrearCita/',login_required(CrearCita), name='Cita_Cirujano'),
    path('ActualizarCita/<int:pk>/', permission_required('base.is_surgeon')(ActualizarCita.as_view()),name='ActualizarCita_Cirujano'),
    path('BorrarCita/<int:pk>', permission_required('base.is_surgeon')(BorrarCita.as_view()),name='BorrarCita_Cirujano'),
    path('Index/',login_required(home_surgeon), name='Index_Cirujano'), 
    path('calendar/', calendar, name='calendar_Cirujano'),
    path('ExpedienteView/<str:id_paciente>',login_required(ExpedienteView), name='ExpedienteView_Cirujano'),
    path('validarCita/', login_required(validarCita),name='validarCita'),
    path('ExpedienteConsulta/<str:id_expediente>', login_required(ExpedienteConsulta),name='ExpedienteConsulta_cirujano'),
    path('ExpedienteSignosVitales/<str:id_expediente>', login_required(ExpedienteSignosVitales),name='SignosVitales_cirujano'),
    path('ExpedienteUpdate/<str:id_expediente>', login_required(ExpedienteUpdate),name='ExpedienteUpdate_cirujano'),
   ]
