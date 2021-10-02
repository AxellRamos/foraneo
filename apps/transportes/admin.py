from django.contrib import admin
from .models import Taxi, Terminal, Bus, HorarioBus


class TaxiAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo', 'municipio')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class TerminalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'municipio', 'hora_apertura', 'hora_cierra')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class BusAdmin(admin.ModelAdmin):
    list_display = ('nombre_transporte', 'ruta', 'terminal')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class HorarioBusAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'hora_salida', 'hora_llegada', 'bus')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


admin.site.register(Taxi, TaxiAdmin)
admin.site.register(Terminal, TerminalAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(HorarioBus, HorarioBusAdmin)
