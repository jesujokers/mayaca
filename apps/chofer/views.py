from django.shortcuts import render
from apps.chofer.forms import *
from apps.chofer.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

# Create your views here.

def index(request):
	return render(request, 'chofer/index.html')

 
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
			login(request, usuario)
			return HttpResponseRedirect(reverse('home:index'))
	else:
		user_form = FormUser
		chofer_form = FormChofer
	return render(request, 'chofer/registro.html', {
		'user_form':user_form,
		'chofer_form':chofer_form
		})

def EditarChofer(request, id_chofer):
	chofer = User.objects.get(id = id_chofer)
	if request.method == 'GET':
		chofer_form = FormChofer(instance = chofer.chofer)
		user_form = FormUser(instance = chofer)
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


def PerfilChofer(request, id_chofer):
	chofer = Chofer.objects.filter(id = id_chofer).exists()
	if chofer == True:
		chofer = Chofer.objects.get(id = id_chofer)
		return render(request, 'chofer/perfil.html', {'chofer': chofer})
	return render(request, 'chofer/perfil.html')

def ListarChofer(request):
	choferes = Chofer.objects.all()
	return render(request, 'chofer/lista.html', {'choferes':choferes})

def Trabajar(request,id_chofer):
	chofer = Chofer.objects.get(id = id_chofer)
	if chofer.trabajando == True:
		chofer.trabajando = False
	else:
		chofer.trabajando = True
	chofer.save()
	return HttpResponseRedirect('/chofer/perfil/' + str(id_chofer))

def Gestion(request):
	return render(request, 'chofer/gestion.html')