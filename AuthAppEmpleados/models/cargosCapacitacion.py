from django.db      import models
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey
from .cargos    import Cargos
from .areaCapacitacion  import AreaCapacitacion


class CargosCapacitacion(models.Model):
    idCarCap = AutoField('id_car_cap', primary_key=True)
    idcarFk = ForeignKey(Cargos,related_name='id_cargo_fk', on_delete=models.CASCADE)
    idAreaCapFk = ForeignKey(AreaCapacitacion, related_name='cargo_area_fk', on_delete=models.CASCADE)
    
