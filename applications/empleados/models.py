from django.db import models
from applications.departamento.models import Departamento

class Empleados(models.Model):

    GENDER_CHOICES=(
        ('M','Masculino'),
        ('F','Femenino'),
    )

    identification = models.IntegerField('Cedula', blank=False, unique=True)
    name = models.CharField('Nombre', max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    civil_status = models.CharField('Estado civil',max_length=10)
    admission_date = models.DateTimeField('Fecha de ingreso', auto_now_add=True, null=True)
    pension_found=models.CharField('Fondo de pensiones',max_length=20)
    eps = models.CharField('Eps', max_length=50)
    phone = models.IntegerField('Telefono')
    compensations = models.CharField('Caja de compensaciones', max_length=50)
    work_city = models.CharField('Ciudad de trabajo', max_length=50)
    gender = models.CharField('Genero',max_length=1, choices=GENDER_CHOICES)
    blood = models.CharField('Tipo de sangre',max_length=5)
    factor = models.CharField('Factor RH',max_length=5)
    job = models.CharField('Cargo',max_length=10)
    disable = models.BooleanField(default=False)

    class Meta:
        verbose_name= "Empleado"
        verbose_name_plural = "empleados de la empresa"

    def __str__(self):
        return str(self.id) + '.' + self.name


