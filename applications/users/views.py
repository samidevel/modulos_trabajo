
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from applications.users.mixins import UserCreatePermissionMixins

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseForbidden


""""
from django.contrib.auth.views import (
    PasswordChangeView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
"""

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from django.core.mail import send_mail


#Formularios del los auth
from .forms import(
    UserRegisterForm,
    UserUpdateForm,
    UserLoginForm,
    UpdatePasswordView,
    PasswordChangeForm,
    UserPasswordReset,
    PasswordResetConfirm
    
    
)

from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    ListView,
    View,
)

from django.views.generic.edit import(
    FormView
)

from .models import User


class ListUserRegister(ListView):
    model = User
    template_name = 'users/list_users.html'
    context_object_name = 'listuser'



class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy('empleados_app:listar_empleados')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Logout_View(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'login_user'
            )
            
        )

class UserCreateView(UserCreatePermissionMixins, FormView):
    template_name = 'users/create_user.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:list_users')
   

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            proyecto=form.cleaned_data['proyecto'],
            ocupation=form.cleaned_data['ocupation'],
            
        )
        return super(UserCreateView, self).form_valid(form)


"""
    def post(self, request, **kwargs):
        if self.request.user.has_perm('users.User.add_user'):
            return HttpResponseRedirect(
                reverse(
                    'users_app:create_user.html'
                )
            )
        else:
            return HttpResponseForbidden()
        
        return super().post(request,  **kwargs)
"""

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users_app:list_users')



class UserUpdatePassword(FormView):

    form_class = UpdatePasswordView
    template_name = 'users/update_pass.html'
    success_url = '.'


class UserPasswordChange(PasswordChangeView):
    template_name = 'users/update_pass.html'
    form_class =   PasswordChangeForm
    success_url = reverse_lazy('users_app:list_users')

    def post(self, request, *args, **kwargs):      
        print(request.POST)
        user = self.request.user
        print(user)
        return super().post(request, *args, **kwargs)
    
class PasswordResetView(FormView):
    template_name = 'users/password_reset.html'
    form_class = UserPasswordReset
    success_url = reverse_lazy('users_app:password_reset_done')
    

class PasswordResetDoneView(FormView):
    template_name = 'users/password_reset_done.html'
    title = ("password modificado con exito")
    
    

class PasswordResetConfirmView(FormView):
    template_name = 'users/reset_confirm_email.html'
    form_class = PasswordResetConfirm
    #send_mail()
    success_url = reverse_lazy('password_reset_confirm')
    

class PasswordCompleteView(FormView):
    template_name = 'users/'

class TurnosView(TemplateView):
    template_name = 'users/turnos_user.html'
    pass