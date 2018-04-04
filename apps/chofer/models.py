from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chofer(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	foto = models.ImageField(upload_to='ChoferFotos/', blank=True)
	cedula = models.CharField(max_length = 8, unique = True)
	telefono = models.CharField(max_length = 12)
	trabajando = models.BooleanField()

	def __str__(self):
		return self.usuario.first_name + ' ' + self.usuario.last_name