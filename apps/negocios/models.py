from django.db import models
from apps.core.models import Base, Municipio

tipoPropietario = (
    (1, 'Uno'),
    (1, 'Dos'),
)


class Propietario(Base):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    correo = models.EmailField()
    cedula = models.CharField(max_length=16)
    direccion = models.TextField()
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    tipo = models.IntegerField(choices=tipoPropietario)

    class Meta:
        verbose_name_plural = 'Propietarios'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombres


class Servicio(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')

    class Meta:
        verbose_name_plural = 'Servicios'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre


class Habitacion(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    ubicacion = models.TextField(max_length='900', verbose_name='Ubicación')
    precio = models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Precio')
    otros_servicios = models.TextField(max_length='900', verbose_name='Otros servicios')
    normas = models.TextField(max_length='256', verbose_name='Normas')
    reglas = models.TextField(max_length='256', verbose_name='Reglas')
    foto = models.URLField(verbose_name="Foto 360")
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT)
    servicio = models.ManyToManyField(Servicio, verbose_name='Servicios')

    class Meta:
        verbose_name_plural = 'Habitaciones'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre


class Comida(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    descripcion = models.TextField(max_length='900', verbose_name='Descripcion')
    foto = models.ImageField(upload_to='habitacion')

    class Meta:
        verbose_name_plural = 'Comida'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre


class Menu(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    foto = models.ImageField(upload_to='menu')
    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Menu'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre


class DetalleMenu(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    foto = models.ImageField(upload_to='menu')
    comida = models.ForeignKey(Comida, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalle Menu'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre
