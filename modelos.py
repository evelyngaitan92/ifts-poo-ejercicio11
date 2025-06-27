from peewee import *
from database import db


class BaseModel(Model):
    class Meta:
        database = db

class Area(BaseModel):
   id_area = AutoField(primary_key=True)
   nombre_area = CharField(unique=True, max_length=80)

class Empleado(BaseModel):
    nro_legajo = IntegerField(unique=True)
    dni= IntegerField(unique=True)
    nombre = CharField(max_length=50, null=False)
    apellido = CharField(max_length=50, null=False)
    area = ForeignKeyField(Area, backref='empleados')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Area: {self.area.nombre_area}"