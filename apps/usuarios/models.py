from django.db import models
from django.contrib.auth.models import User
from apps.core.models import Base, Municipio

SEXOS = (
    (1, 'Hombre'),
    (1, 'Mujer'),
)


class Perfil(Base):
    foto = models.ImageField(upload_to='usuarios')
    cedula = models.CharField(max_length=16, blank=True, null=True)
    carnet = models.CharField(max_length=16, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    sexo = models.IntegerField(choices=SEXOS)
    fecha_nacimiento = models.DateField()
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.usuario.__str__()
