from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
# Create your models here.


class Cliente(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	cedula = models.CharField(max_length = 10)
	telefono = models.CharField(max_length = 12)
	rol = models.CharField(max_length = 20)

class BitacoraCliente(models.Model):
	user = models.ForeignKey(Cliente, on_delete = 'cascade', default = None)
	descripcion = models.CharField(max_length = 20)
	fecha = models.DateField(default = datetime.today)