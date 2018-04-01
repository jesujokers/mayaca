from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.servicio.models import Viaje, Distancia
from apps.cliente.models import Cliente
from apps.chofer.models import Chofer
from datetime import date, datetime


# Create your views here.


def index(request):
	return render(request, 'servicio/index.html')

def pedir(request):
	return render(request, 'servicio/pedir.html')

def confirmar(request):
	if request.method == 'POST':
		origen = request.POST['origen']
		destino = request.POST['destino']
		distancia = request.POST['distancia']
		precio = float(distancia) * 5000
		clientes = Cliente.objects.all()
		contexto = {'origen':origen,
					'destino':destino,
					'distancia':distancia,
					'precio': precio,
					'clientes': clientes
					}
		return render(request, 'servicio/confirmar.html', contexto)	

def RegistrarViaje(request):
	if request.method == 'POST':
		chofer = Chofer.objects.get(trabajando = True)
		cliente = Cliente.objects.get(cedula = request.POST['cliente'])
		cuando = request.POST['fecha']
		fecha = datetime.today()
		precio = 5000

		# if cuando == 'reservar':
		# 	fecha = request.POST['fecha_re']
		distancia = Distancia(
			origen = request.POST['origen'],
			destino = request.POST['destino'],
			distancia = request.POST['distancia']
			)
		distancia.save()
		viaje = Viaje(
			cliente = cliente,
			chofer = chofer,
			fecha_so = fecha,
			fecha_re = fecha,
			origen_destino = distancia,
			precio = precio * float(request.POST['distancia']),
			estado = 'P'
			)
		viaje.save()
		return render(request, 'servicio/pedido.html', {'viaje': viaje, 'distancia': distancia})
	return HttpResponseRedirect(reverse('home:index'))

def DetallesViaje(request,id_viaje):
	viaje = Viaje.objects.filter(id = id_viaje)
	if viaje.exists() == True:
		viaje = Viaje.objects.get(id = id_viaje)
		return render(request, 'servicio/viaje.html', {'viaje':viaje})
	return render(request, 'servicio/viaje.html')

def GestionViajes(request):
	viajes = Viaje.objects.all()
	viajes_p = Viaje.objects.filter(estado = 'P')
	viajes_c = Viaje.objects.filter( estado = 'C')
	viajes_r = Viaje.objects.filter( estado = 'R')
	contexto = {
	'viajes': viajes,
	'viajes_p': viajes_p,
	'viajes_c': viajes_c,
	'viajes_r': viajes_r,
	}
	return render(request, 'servicio/viajes.html', contexto)

def CancelarViaje(request,id_viaje):
	viaje = Viaje.objects.get(id = id_viaje)
	viaje.estado = 'C'
	viaje.save()
	return HttpResponseRedirect(reverse('servicio:gestion'))

def DespacharViaje(request,id_viaje):
	viaje = Viaje.objects.get(id = id_viaje)
	viaje.estado = 'R'
	viaje.save()
	return HttpResponseRedirect(reverse('servicio:gestion'))