from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, CharField

class Cargos(models.Model):
    idCargo = AutoField('id_cargo',primary_key=True)
    cargo = CharField('cargo', max_length=45)
