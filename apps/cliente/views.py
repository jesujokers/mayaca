from django.shortcuts import render
from apps.cliente.forms import *
from django.contrib.auth.models import User
from apps.cliente.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
	return render(request, 'cliente/index.html')

def RegistrarCliente(request):
	if request.method == 'POST':
		form_cliente = FormCliente(request.POST)
		form_user = FormUser(request.POST)
		if form_user.is_valid() and form_cliente.is_valid():
			usuario = form_user.save()
			usuario.refresh_from_db()
			cliente = Cliente(
				usuario = usuario,
				cedula = form_cliente.cleaned_data['cedula'],
				telefono = form_cliente.cleaned_data['telefono'],
				)
			cliente.save()
			login(request, usuario)
			return HttpResponseRedirect(reverse('home:index'))
	else:
		form_cliente = FormCliente
		form_user = FormUser
	return render(request, 'cliente/registro.html',{
		'form_cliente': form_cliente,
		'form_user': form_user
		})
	
def PerfilCliente(request,id_cliente):
	cliente = User.objects.get(id = id_cliente)
	return render(request, 'cliente/perfil.html', {'cliente':cliente})

def EditarCliente(request,id_cliente):
	cliente = User.objects.get(id = id_cliente)
	if request.method == 'GET':
		form_cliente = FormCliente(instance = cliente.cliente)
		form_user = FormUser(instance = cliente)
	else:
		form_cliente = FormCliente(request.POST, instance = cliente)
		form_user = FormUser(request.POST, instance = cliente)
		if form_cliente.is_valid() and form_user.is_valid():
			usuario = form_user.save()
			form_cliente.save()
			login(request, usuario)
			return HttpResponseRedirect(reverse('home:index'))
	return render(request, 'cliente/registro.html',{
		'form_cliente': form_cliente,
		'form_user': form_user
		})