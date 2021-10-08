from django.db                  import models
from django.db.models.fields import EmailField
from .cargos                    import Cargos

class Trabajadores(models.Model):
    cedula = models.BigIntegerField('cedula', primary_key=True)
    nombres = models.CharField('nombres', max_length=50)
    apellidos = models.CharField('apellidos', max_length=50)
    email = models.EmailField('email', max_length=50)
    cargoIdFk = models.ForeignKey(Cargos, related_name='cargo_id_fk', on_delete=models.SET_NULL, null=True)
    