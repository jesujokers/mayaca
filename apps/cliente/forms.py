from apps.cliente.models import *

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
class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'cedula',
			'telefono',
		]
		labels = {
			'cedula': 'Cedula',
			'telefono': 'Telefono',
		}