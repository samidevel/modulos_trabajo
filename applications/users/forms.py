#importar los formularios de django
from django import forms
#importar el modelo usuarios
from .models import User
from django.contrib.auth import authenticate

from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm




class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username',required=True, 
                                widget=forms.TextInput(attrs={'placeholder':'Ingrse su usaurio'}))
    password = forms.CharField(label='Contraseña',required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder':'contraseña'}))
    def clean(self):
        cleaned_data=super(UserLoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos no son corrrectos')
        return self.cleaned_data


"""
class UserRegisterForm(UserCreationForm):
    pass
"""

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña',required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))
    password2 = forms.CharField(label='Contraseña',required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder':'Repetir contraseña'}))

    class Meta:
        model= User
        fields=(
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'proyecto',
            'ocupation',
            'password1',
            'password2',
            'is_staff',
            
        )
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'usuario', 'class':'input-group-field'}),
            'email': forms.EmailInput(attrs={'placeholder':'Ingrese el email', 'class':'input-group-field'}),
            'nombres': forms.TextInput(attrs={'placeholder':'ingrese nombres', 'class':'input-group-field'}),
            'apellidos': forms.TextInput(attrs={'placeholder':'ingrese apellidos'})
        }
        

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password1', "Las contraseñas no son iguales")



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=(
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            'proyecto',
            'is_staff',
            'is_active',
        )


class UpdatePasswordView(forms.Form):
    password1 = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña actual'}))
    password2 = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña Nueva'}))


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Actual', required=True, widget=forms.PasswordInput(attrs={'placeholder':'contraseña actual'}))
    new_password1 = forms.CharField(label='Nueva Contraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder':'Nueva contraseña'}))
    new_password2 = forms.CharField(label='Repetir Conraseña', required=True, widget=forms.PasswordInput(attrs={'placeholder':'Repetir Contraseña'}))

    class Meta:
        model = User
        fields=('ol_password', 'new_password1', 'new_password2')

   

class UserPasswordReset(PasswordResetForm):
    email = forms.EmailField(label='correo', required=True, widget=forms.EmailInput(attrs={'placeholder':'Ingrese el email a restablecer'}))
    class Meta:
        model = User
        fields= ('email')


class PasswordResetConfirm(forms.Form):
    password1 = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña actual'}))
    password2 = forms.CharField(label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'placeholder':'Contraseña Nueva'}))



