from django.db import models
from apps.cliente.models import Cliente 
from apps.chofer.models import Chofer 
from datetime import datetime 
from django.contrib.auth.models import User


# Create your models here.

class Distancia(models.Model):
	origen = models.CharField(max_length = 150)
	destino = models.CharField(max_length = 150)
	distancia = models.FloatField()


class BitacoraViaje(models.Model):
	descripcion = models.CharField(max_length = 30)
	fecha = models.DateField(datetime.today)
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)

class Viaje(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	chofer = models.ForeignKey(Chofer, on_delete = models.CASCADE)
	fecha_so = models.DateTimeField(auto_now_add=True, blank=True)
	fecha_re = models.DateTimeField()
	origen_destino = models.ForeignKey(Distancia, on_delete = models.CASCADE)
	precio = models.FloatField()
	estado = models.CharField(max_length = 1)

