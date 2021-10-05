from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, CharField, DateTimeField
from django.db.models.fields.related import ForeignKey

from .areaCapacitacion import AreaCapacitacion


class Capacitacion(models.Model):
    idCapacitacion = AutoField('id_capacitacion',primary_key=True)
    curso = CharField('curso', max_length=45)
    idAreaCapacitacionFk = ForeignKey(AreaCapacitacion, related_name='id_area_cap', on_delete=models.CASCADE)
    fecha = DateTimeField('fecha')
