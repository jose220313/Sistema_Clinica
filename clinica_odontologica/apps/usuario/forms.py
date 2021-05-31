from django.contrib.auth.forms import AuthenticationForm
from django import forms

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super (FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'usuario'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'password'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password'].widget.attrs['type'] = 'password'