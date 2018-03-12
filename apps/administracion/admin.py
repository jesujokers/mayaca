from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Empleado)
admin.site.register(BitacoraEmpleado)
admin.site.register(Permisos)
