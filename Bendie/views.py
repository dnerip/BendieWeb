from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

def index(request, template_name = 'bendie/index.html'):
	"""
	Función vista para la página inicio del sitio.
	"""
	rooms = Room.objects.all()

	template_rooms = []

	for room in rooms:
		lights = Light.objects.filter(room = room)
		blinds = Blind.objects.filter(room = room)
		sensors = Sensor.objects.filter(room = room)
		doors = Door.objects.filter(room = room)
		devices = len(lights) + len(blinds) + len(sensors) + len(doors)
		template_rooms.append([room, devices]) 
		devices = 0

	for t in template_rooms:
		print(t[0].name)


	# Renderiza la plantilla HTML index.html con los datos en la variable contexto
	return render(request, template_name, locals(),)


@login_required
def devices(request, id_room, template_name = 'bendie/devices.html'):
	"""
	Función vista para la página de habitaciones.
	"""
	room = Room.objects.get(id = id_room)

	lights = Light.objects.filter(room = room)
	blinds = Blind.objects.filter(room = room)
	sensors = Sensor.objects.filter(room = room)
	doors = Door.objects.filter(room = room)

	return render(request, template_name, locals(),)

#@login_required
#def room_devices(request):