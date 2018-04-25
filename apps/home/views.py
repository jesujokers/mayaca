from django.shortcuts import render


# Create your views here.


def index(request):
	return render(request, 'home/index.html')

def acerca_de(request):
	return render(request, 'home/acerca-de.html')

def terminos(request):
	return render(request, 'acerca-de/terminos.html')