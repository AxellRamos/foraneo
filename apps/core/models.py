from crum import get_current_user
from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from solo.models import SingletonModel


class Base(models.Model):
    usuario_grabacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_grabacion_%(class)s',
                                          blank=True, null=True)
    fecha_grabacion = models.DateTimeField(auto_now_add=True)
    usuario_modificacion = models.ForeignKey(User, related_name='usuario_modificacion_%(class)s',
                                             on_delete=models.PROTECT, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_grabacion = user
        self.usuario_modificacion = user
        super().save(*args, **kwargs)

    def to_json(self):
        return model_to_dict(self)


class Departamento(models.Model):
    nombre = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Departamentos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=64)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Municipios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
