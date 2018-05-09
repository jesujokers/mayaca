from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.


class Permisos(models.Model):
	agregar = models.BooleanField()
	eliminar = models.BooleanField()
	editar = models.BooleanField()
	suspender = models.BooleanField()
	habilitar = models.BooleanField()


class Empleado(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='EmpleadoFotos/', blank=True)
	cedula = models.CharField(max_length = 10, blank = True, unique= True)
	sueldo = models.FloatField(blank = True)
	fecha_nacimiento = models.DateField(null=True, blank=True, default=None)
	direccion = models.CharField(max_length = 80, blank = True)
	telefono = models.CharField(max_length = 14, blank = True)
	rol = models.CharField(max_length = 20, blank = True)
	permisos = models.OneToOneField(Permisos, on_delete=models.CASCADE)

	def __str__(self):
		return self.usuario.username + ' ' + self.usuario.last_name

class BitacoraEmpleado(models.Model):
	user = models.ForeignKey(User, on_delete = 'cascade', default = None)
	descripcion = models.CharField(max_length = 12)
	fecha = models.DateField(default=datetime.today)

