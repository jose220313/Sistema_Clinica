from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy,reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from .forms import FormularioLogin

class Login (FormView):
    template_name='registration/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Index1')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
       if request.user.is_authenticated:
           if request.user.has_perm('base.is_surgeon'):
               print('Es cirujano')
               return HttpResponseRedirect(reverse_lazy('Index'))
           if request.user.has_perm('base.is_secretary'):
               print('Es secretaria')
               return HttpResponseRedirect(reverse_lazy('Index1'))
           if request.user.has_perm('base.is_doctor'):
               print('Es Doctor')
               return HttpResponseRedirect(reverse_lazy('Index2'))
           print('Está autenticado')
       else:
            return super(Login,self).dispatch(request, *args, **kwargs)        
    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

# Create your views here.
