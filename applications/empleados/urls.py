from django.urls import path, include
from .import views

app_name = "empleados_app"

urlpatterns = [
    path('listar-empleados', views.ListEmpleados.as_view(), name="listar_empleados"),
    path('listar-by-departamento/<shor_name>/', views.ListBYAreaEmpleados.as_view(),
          name="listar_departamento"), 
    path('filtar-identification/<identification>/', views.FilterIdentification.as_view()),
    path('ListEmpledos-Formu', views.ListEmpledosFormu.as_view()),
    path('detail-empleado/<pk>/', views.EmpleadoDetail.as_view(), name='detail_empleado'),
    path('create-empleado', views.EmpleadoCreateView.as_view()),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name="update_empleado"),
    path('success-url', views.SuccessView.as_view(), name="success"),
    path('success-update', views.SuccessUpdate.as_view(), name="success_update"),
    
]