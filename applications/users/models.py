from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    ADMINISTRADOR = '0'
    ANALISTA = '1'

    PERMISSIONS_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ANALISTA, 'Analista'),
    ]

    GENERO_CHOICES=(
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )


    ALGAR='0'
    SOPORTE='1'
    PROYECTO_CHOICES= [
        (ALGAR, 'Algar'),
        (SOPORTE, 'Soporte'),
    ]
       
    
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    ocupation = models.CharField(max_length=1, choices=PERMISSIONS_CHOICES, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True)
    proyecto = models.CharField(max_length=10, choices=PROYECTO_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 

    objects = UserManager()




    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres +''+ self.apellidos




"""
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
"""