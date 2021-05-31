from django.urls import path
from apps.secretaria.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('Paciente/', login_required(CrearPaciente),name='Paciente'),
    path('VerPaciente/', login_required(VerPaciente),name='VerPaciente'),
    path('AgregarExpediente/<id_paciente>', login_required(AgregarExpediente.as_view()),name='AgregarExpediente'),
    path('ActualizarPaciente/<str:id_paciente>', login_required(ActualizarPaciente), name='ActualizarPaciente'),
    path('buscar/', login_required(buscar),name='buscar'),
    path('CrearCita/',login_required(CrearCita), name='Cita'), 
    path('ActualizarCita/<int:pk>',login_required(ActualizarCita.as_view()),name='ActualizarCita'),
    path('BorrarCita/<int:pk>', login_required(BorrarCita.as_view()),name='BorrarCita'),
    path('Index/',login_required(home_secretary), name='Index1'), 
    path('calendar/', calendar, name='calendar'),
    path('ExpedienteView/<str:id_paciente>',login_required(ExpedienteView), name='ExpedienteView'),
    path('validarCita/', login_required(validarCita),name='validarCita'),
   ]
