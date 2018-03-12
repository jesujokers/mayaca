from django.db import models
from apps.cliente.models import Cliente 
from apps.chofer.models import Chofer 


# Create your models here.

class Distancia(models.Model):
	origen = models.CharField(max_length = 150)
	destino = models.CharField(max_length = 150)
	distancia = models.FloatField()


class Viaje(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
	chofer = models.ForeignKey(Chofer, on_delete = models.CASCADE)
	fecha_so = models.DateField()
	fecha_re = models.DateField()
	origen_destino = models.ForeignKey(Distancia, on_delete = models.CASCADE)
	precio = models.FloatField()
	estado = models.BooleanField()
