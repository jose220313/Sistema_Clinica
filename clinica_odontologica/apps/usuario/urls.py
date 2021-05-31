from django.urls import path
from apps.usuario.views import Login, logoutUsuario
from apps.secretaria.views import home_secretary
from apps.base.views import home_surgeon
from apps.doctor.views import home_doctor
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('',Login.as_view(),name = 'Login'),
    path('logout/',logoutUsuario,name = 'logout'),
    path('base/Index',home_surgeon, name='Index'),
    path('secretaria/Index',home_secretary,name='Index1'),
    path('doctor/Index',home_doctor,name='Index2'),
   ]