# Generated by Django 4.1.7 on 2023-03-20 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.IntegerField(unique=True, verbose_name='Cedula')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('civil_status', models.CharField(max_length=10, verbose_name='Estado civil')),
                ('admission_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de ingreso')),
                ('pension_found', models.CharField(max_length=20, verbose_name='Fondo de pensiones')),
                ('eps', models.CharField(max_length=50, verbose_name='Eps')),
                ('phone', models.IntegerField(verbose_name='Telefono')),
                ('compensations', models.CharField(max_length=50, verbose_name='Caja de compensaciones')),
                ('work_city', models.CharField(max_length=50, verbose_name='Ciudad de trabajo')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero')),
                ('blood', models.CharField(max_length=5, verbose_name='Tipo de sangre')),
                ('factor', models.CharField(max_length=5, verbose_name='Factor RH')),
                ('job', models.CharField(max_length=10, verbose_name='Cargo')),
                ('disable', models.BooleanField(default=False)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'empleados de la empresa',
            },
        ),
    ]
