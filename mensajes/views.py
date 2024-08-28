# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tablero
#from .models import Tarea

def mensajes_recibidos(request):
# Se interactúa con el modelo para obtener las tareas pendientes
    mensajes_recibidos = Tablero.objects.filter(remitente='gonzalo')
# Se pasa la lista de tareas a la plantilla
    return render(request, 'mensajesRecibidos.html', {'mensajes': mensajes_recibidos})
    return HttpResponse("hola") 