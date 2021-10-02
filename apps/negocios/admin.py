from django.contrib import admin
from .models import Propietario, Habitacion, Comida, Menu, DetalleMenu, Servicio


class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'correo', 'cedula')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'propietario')
    filter_horizontal = ('servicio',)
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class ComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'propietario')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


class DetalleMenuAdmin(admin.ModelAdmin):
    list_display = ('comida', 'menu')
    exclude = ('usuario_grabacion', 'usuario_modificacion')


admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Comida, ComidaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(DetalleMenu, DetalleMenuAdmin)
admin.site.register(Servicio, ServicioAdmin)
