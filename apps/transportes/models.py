from django.db import models
from apps.core.models import Base, Municipio


class Taxi(Base):
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    correo = models.EmailField()
    cedula = models.TextField()
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to='taxi')
    placa = models.CharField(max_length=16)
    ubicacion = models.TextField()
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Taxis'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombres


class Terminal(Base):
    nombre = models.CharField(max_length=128)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    hora_apertura = models.TimeField(verbose_name='Hora de Inicio')
    hora_cierra = models.TimeField(verbose_name='Hora de Finalización')

    class Meta:
        verbose_name_plural = 'Terminales'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre


class Bus(Base):
    nombre_transporte = models.CharField(max_length=128)
    ruta = models.TextField()
    terminal = models.ForeignKey(Terminal, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Bus'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.nombre_transporte


class HorarioBus(Base):
    origen = models.CharField(max_length=128)
    destino = models.CharField(max_length=128)
    hora_salida = models.TimeField(verbose_name='Hora de Inicio')
    hora_llegada = models.TimeField(verbose_name='Hora de Finalización')
    bus = models.ForeignKey(Bus, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Horarios'
        ordering = ['-fecha_grabacion']

    def __str__(self):
        return self.origen
