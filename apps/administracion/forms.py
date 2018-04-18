from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.administracion.models import *

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
 

class FormUser(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			]
		labels = {
			'username' : 'Nombre de Usuario',
			'first_name': 'Nombre',
			'last_name': 'Apeliido' ,
			'email': 'Correo Electronico',
		}

class FormEmpleado(forms.ModelForm):
	class Meta:
		model = Empleado 
		fields = (
			'cedula',
			'sueldo',
			'fecha_nacimiento',
			'direccion',
			'telefono',
			'foto'
			)
		labels = {
			'cedula': 'Cedula',
			'sueldo': 'Sueldo',
			'fecha_nacimiento': 'Fecha Nacimiento',
			'direccion': 'Direccion',
			'telefono': 'Telefono',
			'foto': 'Foto del Empleado',
		}

class FormPermisos(forms.ModelForm):
	class Meta:
		model = Permisos
		fields = (
			'agregar',
			'eliminar',
			'editar',
			'actualizar',
			'suspender',
			'habilitar'
			)
		labels = {
			'agregar': 'Agregar',
			'eliminar': 'Eliminar',
			'editar': 'Editar',
			'actualizar': 'Actualizar',
			'suspender': 'Suspender',
			'habilitar': 'Habilitar',
		}
