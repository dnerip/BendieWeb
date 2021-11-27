from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Room)
admin.site.register(Light)
admin.site.register(Blind)
admin.site.register(Sensor)
admin.site.register(Door)