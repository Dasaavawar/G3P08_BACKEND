from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import AutoField, CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from .areaCapacitacion       import AreaCapacitacion

class Capacitacion(models.Model):
    idCapacitacion = AutoField('id_capacitacion', primary_key=True)
    curso = CharField('curso', max_length=45)
    idAreaCapacitacionFk = ForeignKey(AreaCapacitacion, related_name='capacitacion_area_fk', on_delete=SET_NULL, null=True)
    fecha = DateTimeField('fecha')