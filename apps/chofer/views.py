from django.shortcuts import render
from apps.chofer.forms import *
from apps.chofer.models import *
from apps.administracion.models import Empleado
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.

def index(request):
	return render(request, 'chofer/index.html')

 
def EliminarChofer(request,id_chofer):
	usuario_actual = request.user.id 
	empleado = Empleado.objects.filter(usuario = usuario_actual)
	if empleado.exists() == True:
		chofer = Chofer.objects.filter(id = id_chofer)
		if chofer.exists() == True:
			chofer = Chofer.objects.get(id = id_chofer)
			id_user = chofer.usuario_id
			print(id_user)
			usuario = User.objects.get(id = id_user)
			chofer.delete()
			usuario.delete()
			return HttpResponseRedirect(reverse('chofer:listar'))
	return HttpResponseRedirect(reverse('home:index'))

def RegistrarChofer(request):
	if request.method == 'POST':
		user_form = FormUser(request.POST)
		chofer_form = FormChofer(request.POST, request.FILES)
		if user_form.is_valid() and chofer_form.is_valid():
			usuario = user_form.save()
			usuario.refresh_from_db()
			chofer = Chofer(
				usuario = usuario,
				cedula = chofer_form.cleaned_data['cedula'],
				telefono = chofer_form.cleaned_data['telefono'],
				trabajando = True,
				foto = request.FILES['foto']
				)
			chofer.save()
			usuario.is_active = 0
			usuario.save()
			return HttpResponseRedirect(reverse('home:index'))
	else:
		user_form = FormUser
		chofer_form = FormChofer
	return render(request, 'chofer/registro.html', {
		'user_form':user_form,
		'chofer_form':chofer_form
		})
	return HttpResponseRedirect(reverse('home:index'))

def EditarChofer(request, id_chofer):
	if request.user.is_authenticated:
		# Verificar si es empleado
		bandera = False
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True:
			chofer = Chofer.objects.filter(id = id_chofer)
			if chofer.exists() == True:
				chofer = Chofer.objects.get(id = id_chofer)
				bandera = True
		# Verificar si es el dueño de la cuenta el que intenta acceder
		chofer = Chofer.objects.filter(id = id_chofer)
		if chofer.exists() == True:
			chofer = Chofer.objects.get(id = id_chofer)
			if chofer.usuario_id == usuario_actual:
				bandera = True

	if bandera == True:
		chofer = Chofer.objects.get(id = id_chofer)
		if request.method == 'GET':
			chofer_form = FormChofer(instance = chofer)
			user_form = FormUser(instance = chofer.usuario)
		else:
			chofer_form = FormChofer(request.POST, request.FILES, instance = chofer)
			user_form = FormUser(request.POST, instance = chofer)
			if chofer_form.is_valid() and user_form.is_valid():
				usuario = user_form.save()
				chofer_form.save()
				login(request, usuario)
				return HttpResponseRedirect(reverse('home:index'))
		return render(request, 'chofer/registro.html',{
			'chofer_form': chofer_form,
			'user_form': user_form
			})
	return HttpResponseRedirect(reverse('home:index'))
 
def PerfilChofer(request, id_chofer):
	if request.user.is_authenticated:
		# Verificar si es empleado
		bandera = False
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True:
			chofer = Chofer.objects.filter(id = id_chofer)
			if chofer.exists() == True:
				chofer = Chofer.objects.get(id = id_chofer)
				bandera = True
		# Verificar si es el dueño de la cuenta el que intenta acceder
		chofer = Chofer.objects.filter(id = id_chofer)
		if chofer.exists() == True:
			chofer = Chofer.objects.get(id = id_chofer)
			if chofer.usuario_id == usuario_actual:
				bandera = True
		if bandera == True:
			return render(request, 'chofer/perfil.html', {'chofer': chofer,'bandera':bandera})
	return render(request, 'chofer/perfil.html')

def ListarChofer(request):
	if request.user.is_authenticated:
		usuario_actual = request.user.id
		empleado = Empleado.objects.filter(usuario_id = usuario_actual)
		if empleado.exists() == True:
			choferes = Chofer.objects.all()
			bandera = True
			return render(request, 'chofer/lista.html', {'choferes':choferes,'bandera':bandera})
	return render(request, 'chofer/lista.html')
		

def Trabajar(request,id_chofer):
	if request.user.is_authenticated:
		# Verificar si es empleado
		bandera = False
		usuario_actual = request.user.id 
		empleado = Empleado.objects.filter(usuario = usuario_actual)
		if empleado.exists() == True:
			chofer = Chofer.objects.filter(id = id_chofer)
			if chofer.exists() == True:
				chofer = Chofer.objects.get(id = id_chofer)
				bandera = True
		# Verificar si es el dueño de la cuenta el que intenta acceder
		chofer = Chofer.objects.filter(id = id_chofer)
		if chofer.exists() == True:
			chofer = Chofer.objects.get(id = id_chofer)
			if chofer.usuario_id == usuario_actual:
				bandera = True
	if bandera == True:
		chofer = Chofer.objects.get(id = id_chofer)
		if chofer.trabajando == True:
			chofer.trabajando = False
		else:
			chofer.trabajando = True
		chofer.save()
		return HttpResponseRedirect('/chofer/perfil/' + str(id_chofer))
	return HttpResponseRedirect(reverse('home:index'))

def Gestion(request):
	return render(request, 'chofer/gestion.html')