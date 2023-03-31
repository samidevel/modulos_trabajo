from django.contrib import admin
from .models import Empleados

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'identification',
        'name',
        'civil_status',
        'admission_date',
        'pension_found',
        'eps',
        'phone',
        'compensations',
        'work_city',
        'gender',
        'blood',
        'factor',
        'job',
        'departamento',
        'full_name',
    )

    def full_name(self , obj):
        print(obj.departamento)
        return 'prueba'

    search_fields = ('identification',)
    list_filter = ('job', 'departamento')
    #filter_horizontal = ('',)


admin.site.register(Empleados, EmpleadoAdmin)
