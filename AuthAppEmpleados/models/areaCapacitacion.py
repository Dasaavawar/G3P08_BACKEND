from django.db          import models
from django.db.models.fields import AutoField, CharField

class AreaCapacitacion(models.Model):
    idAreaCap = AutoField('id_area_capacitacion', primary_key=True)
    area = CharField('area', max_length=45)
    descripcion = CharField('descripcion', max_length=100)
    

