from django.shortcuts import render
from apps.cliente.forms import *
from django.contrib.auth.models import User
from apps.cliente.models import *
from apps.servicio.models import *
from apps.administracion.models import Empleado
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
	cliente = Cliente.objects.get(id = id_cliente)
	return render(request, 'cliente/perfil.html', {'cliente':cliente})

def EditarCliente(request,id_cliente):
	bandera = False
	bandera2 = False
	usuario_actual = request.user.id 

	# Comprobacion de si es el cliente actual
	cliente = Cliente.objects.filter(id = id_cliente)
	if cliente.exists() == True:
		cliente = Cliente.objects.filter(usuario = usuario_actual)
		if cliente.exists() == True:
			cliente = Cliente.objects.get(usuario = usuario_actual)
			if id_cliente == cliente.id:
				bandera = True

	# Comprobacion de si es un empleado 
	empleado = Empleado.objects.filter(usuario = usuario_actual)
	if empleado.exists() == True:
		empleado = Empleado.objects.get(usuario = usuario_actual)
		if empleado.usuario.id == usuario_actual:
			bandera2 = True

	if request.user.is_authenticated and (bandera2 == True or bandera == True):
		cliente = Cliente.objects.get(id = id_cliente)
		if request.method == 'GET':
			form_cliente = FormCliente(instance = cliente)
			form_user = FormUser(instance = cliente.usuario)
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
	else:
		return render(request, 'cliente/registro.html')

def ViajesCliente(request, id_cliente):
	if request.user.is_authenticated:
		usuario_actual = request.user.id
		bandera = False
		bandera2 = False

		cliente = Cliente.objects.filter(usuario_id = usuario_actual)
		# Verificar que el usuario si existe como cliente...
		if cliente.exists() == True:
			bandera = True
		# Verificar si el usuario actual coincide con la solicitud 
		if bandera == True:
			cliente = Cliente.objects.get(usuario_id = usuario_actual)
			if id_cliente == cliente.id:
				bandera2 = True
		# Mostrar los viajes si las dos validaciones anteriores se cumplieron
		if bandera == True and bandera2 == True:
			viajes = Viaje.objects.filter(cliente_id = id_cliente)
			viajes_p = Viaje.objects.filter(cliente_id = id_cliente, estado = 'P')
			viajes_c = Viaje.objects.filter(cliente_id = id_cliente, estado = 'C')
			viajes_r = Viaje.objects.filter(cliente_id = id_cliente, estado = 'R')
			contexto = {
			'viajes': viajes,
			'viajes_p': viajes_p,
			'viajes_c': viajes_c,
			'viajes_r': viajes_r,
			}
			return render(request, 'cliente/servicio.html', contexto)
	return HttpResponseRedirect(reverse('home:index'))

def ListarClientes(request):
	no = False
	if request.user.is_authenticated:
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True: 
			clientes = Cliente.objects.all()
			return render(request, 'cliente/lista.html', {'clientes':clientes})
	no = True
	return render(request, 'cliente/lista.html',{'no':no})