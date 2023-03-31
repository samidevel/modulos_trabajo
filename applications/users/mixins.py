from .models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse



def check_ocupation_user(ocupation, user_ocupation):
    
    if (ocupation == User.ADMINISTRADOR or ocupation == user_ocupation):
        
        return True
    else:
        return False
    

class UserCreatePermissionMixins(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:list_users')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'empleados_app:listar_empleados'
                )
            )
        return super().dispatch(request, *args, **kwargs)
    


class EmpleadoObjectsMixins(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:list_users')
        
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not check_ocupation_user(request.user.ocupation, User.ANALISTA):
            # no tiene autorizacion
            return HttpResponseRedirect(
                reverse(
                    'empleados_app:listar_empleados'
                )
            )
        

        return super().dispatch(request, *args, **kwargs)