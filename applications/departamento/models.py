from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre corto', max_length=10)
    active = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Depatamento'
        verbose_name_plural= "Departamento"
        ordering = ['-name']

    def __str__(self):
        return self.name + '-' + self.shor_name
    



    


