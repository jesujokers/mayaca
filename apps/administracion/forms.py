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
			'last_name': 'Apellido' ,
			'email': 'Correo Electronico',
		}
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
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
		widgets = {
			'cedula': forms.TextInput(attrs={'class':'form-control', 'required': ''}),
			'sueldo': forms.TextInput(attrs={'class':'form-control', 'required': ''}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control', 'required': ''}),
			'direccion': forms.TextInput(attrs={'class':'form-control', 'required': ''}),
			'telefono': forms.TextInput(attrs={'class':'form-control', 'required': ''}),
		}

class FormPermisos(forms.ModelForm):
	class Meta:
		model = Permisos
		fields = (
			'agregar',
			'eliminar',
			'editar',
			'suspender',
			'habilitar'
			)
		labels = {
			'agregar': 'Agregar',
			'eliminar': 'Eliminar',
			'editar': 'Editar',
			'suspender': 'Suspender',
			'habilitar': 'Habilitar',
		}
