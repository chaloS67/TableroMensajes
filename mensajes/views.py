# views.py
from django.http import HttpResponse
from django.shortcuts import render
#from .models import Tarea

def mensajes_recibidos(request):
# Se interactúa con el modelo para obtener las tareas pendientes
#ver_tareas_pendientes = Tarea.objects.filter(estado='pendiente')
# Se pasa la lista de tareas a la plantilla
#return render(request, 'tareas/pendientes.html', {'tareas': tareas_pendientes})
    return HttpResponse("hola") 