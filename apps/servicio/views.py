from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'servicio/index.html')

def pedir(request):
	return render(request, 'servicio/pedir.html')

def confirmar(request):
	origen = request.POST['origen']
	destino = request.POST['destino']
	distancia = request.POST['distancia']
	precio = 25000
	cliente = request.user.id
	contexto = {'origen':origen,
				'destino':destino,
				'distancia':distancia,
				'precio': precio
				}
	return render(request, 'servicio/confirmar.html', contexto)	