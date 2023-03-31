from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.users.mixins import EmpleadoObjectsMixins


from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from .models import Empleados

class IndexView(TemplateView):
    template_name= "home.html"


class ListEmpleados(EmpleadoObjectsMixins, ListView):
    #model = Empleados
    template_name = "empleados/lista_empleados.html"
    context_object_name = "listar_empleados"
    paginate_by=2
    login_url = reverse_lazy('users_app:login_user')
    #ordering =""

    def get_queryset(self):
        buscar_cedula = self.request.GET.get("kward", '')
        lis = Empleados.objects.filter(identification__icontains=buscar_cedula)
        return lis


class FilterIdentification(EmpleadoObjectsMixins,ListView):
    #filtar mediante kwargs
    template_name = "empleados/lista_identi.html"
    #context_object_name= "for_empleados"
    def get_queryset(self):
        ident= self.kwargs['identification']
        emp = Empleados.objects.filter(identification=ident)
        return emp
        


#List view para empleados mediante un formulario
class ListEmpledosFormu(EmpleadoObjectsMixins,ListView):
    template_name = "empleados/ListEmpformu.html"
    context_object_name = "empleados"

    def get_queryset(self):
    
        buscar_cedula = self.request.GET.get("kward",)
        lis = Empleados.objects.filter(
            identification=buscar_cedula
            )
        return lis



#List view para buscar por cedula
class ListBYAreaEmpleados(EmpleadoObjectsMixins,ListView):
    template_name = "empleados/lista_identi.html" 
    def get_queryset(self):
        area = self.kwargs['shor_name']
        lista = Empleados.objects.filter(
            departamento__name=area
            )
        return lista
    

class EmpleadoDetail(EmpleadoObjectsMixins,DetailView):
    model = Empleados
    template_name = "empleados/det_empleado.html"
    context_object_name="empleado"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetail, self).get_context_data(**kwargs)
        return context
    


class SuccessView(TemplateView):
    template_name = "empleados/success_url.html"
    
class EmpleadoCreateView(EmpleadoObjectsMixins,CreateView):
    model = Empleados
    template_name = "empleados/create_empleado.html"
    fields = '__all__'
    success_url = reverse_lazy('empleados_app:success')


class SuccessUpdate(TemplateView):
    template_name = "empleados/succes_update.html"

class EmpleadoUpdateView(EmpleadoObjectsMixins,UpdateView):
    model = Empleados
    fields = '__all__'
    template_name = "empleados/update_empleado.html"
    success_url = reverse_lazy('empleados_app:success_update')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("***post***")
        print("----")
        print(request.POST)
        var_identification=request.POST['identification']
        print(var_identification)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("form valid")
        print("***")
        return super(EmpleadoUpdateView, self).form_valid(form)

