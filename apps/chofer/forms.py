from apps.chofer.models import * 
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

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
class FormChofer(forms.ModelForm):
	class Meta:
		model = Chofer 
		fields = [
			'cedula',
			'telefono',
			'foto',
		]
		labels = {
			'cedula': 'Cedula',
			'telefono': 'Telefono',
			'foto': 'Foto',
		}