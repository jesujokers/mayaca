from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chofer(models.Model):
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	cedula = models.CharField(max_length = 8)
	telefono = models.CharField(max_length = 12)
	trabajando = models.BooleanField()