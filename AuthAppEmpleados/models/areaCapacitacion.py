from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, CharField


class AreaCapacitacion(models.Model):
    idAreaCap = AutoField('id_area_cap', primary_key=True)
    area = CharField('area', max_length=45)
    descripcion = CharField('descripcion', max_length=100)
