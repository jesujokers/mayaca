from django.shortcuts import render
from apps.administracion.forms import FormUser, FormEmpleado, FormPermisos
from apps.administracion.models import *
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy,reverse
from apps.servicio.models import *

# from django.urls import reverse
# from django.utils.functional import lazy
# reverse_lazy = lambda *args, **kwargs: lazy(reverse, str)(*args, **kwargs) 


# Create your views here.

def index(request):
	return render(request, 'administracion/index.html')

class RegistroUsuario(CreateView):
	model = User 
	form_class = FormUser
	template_name = 'administracion/registro.html' 
	success_url = reverse_lazy('administracion/listar')

class UsuarioListar(ListView):
	model = User
	template_name = 'administracion/lista.html'
	paginate_by = 4

class UsuarioDelete(DeleteView):
	model = User 
	template_name = 'administracion/delete.html'
	success_url = reverse_lazy('administracion:listar')

class UsuarioUpdate(UpdateView):
	model = User 
	template_name = 'administracion/registro.html'
	form_class = FormUser
	success_url = reverse_lazy('home:index')

def Suspender(request, id_usuario):
	usuario = User.objects.get(id = id_usuario)
	usuario.is_active = 0
	if request.method == 'POST':
		usuario.save()
		return HttpResponseRedirect(reverse('administracion:listar'))
	return render(request,'administracion/suspender.html', {'usuario':usuario})

def Habilitar(request, id_usuario):
	usuario = User.objects.get(id = id_usuario)
	usuario.is_active = 1
	if request.method == 'POST':
		usuario.save()
		return HttpResponseRedirect(reverse('administracion:listar'))
	return render(request,'administracion/habilitar.html', {'usuario':usuario})



def RegistrarEmpleado(request):
	if request.method == 'POST':
		user_form = FormUser(request.POST)
		empleado_form = FormEmpleado(request.POST)
		permisos_form = FormPermisos(request.POST)
		if empleado_form.is_valid() and user_form.is_valid() and permisos_form.is_valid():
			user = user_form.save()
			user.refresh_from_db()
			permisos = permisos_form.save()
			empleado = Empleado(
				usuario = user, 
				cedula = empleado_form.cleaned_data['cedula'],
				sueldo = empleado_form.cleaned_data['sueldo'],
				fecha_nacimiento = empleado_form.cleaned_data['fecha_nacimiento'],
				direccion = empleado_form.cleaned_data['direccion'],
				telefono = empleado_form.cleaned_data['telefono'],
				rol = empleado_form.cleaned_data['rol'],
				permisos = permisos
				)
			empleado.save()
			bitacora = BitacoraEmpleado(
				user = empleado,
				descripcion = "Registro"
				)
			bitacora.save()
			login(request, user)
			return HttpResponseRedirect(reverse('home:index'))
	else:
		user_form = FormUser
		empleado_form = FormEmpleado
		permisos_form = FormPermisos
	return render(request, 'administracion/registro.html',{
       	'user_form': user_form,
       	'empleado_form': empleado_form,
       	'permisos_form': permisos_form
       	})


def ListarEmpleado(request):
	empleados = Empleado.objects.all()
	contexto = {'empleados': empleados}
	return render(request, 'administracion/lista.html', contexto)

def PerfilEmpleado(request, id_usuario):
	usuario = User.objects.get(id = id_usuario)
	return render(request, 'administracion/perfil.html', {'usuario':usuario})

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
	return render(request, 'administracion/viajes.html', contexto)

def Panel(request):
	return render(request, 'administracion/panel.html')