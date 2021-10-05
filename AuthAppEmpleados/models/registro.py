from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from .capacitacion import Capacitacion
from .trabajadores import Trabajadores

class Registro(models.Model):
    idRegistro = AutoField('id_registro', primary_key=True)
    idCapacitacionFk = ForeignKey(Capacitacion, related_name='id_capacitacion_fk', on_delete=CASCADE)
    cedulaTrabajador = ForeignKey(Trabajadores, related_name='cedula_trabajador', on_delete=CASCADE)
