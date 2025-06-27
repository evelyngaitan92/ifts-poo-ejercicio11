from peewee import *
from database import db


class BaseModel(Model):
    class Meta:
        database = db

# La estructura de la tabla Areas deberá ser la siguiente: 
# • id int PRIMARY KEY AUTOINCREMENTAL NOT NULL 
# • nombre_area text NOT NULL UNIQUE MAX_LENGTH=80 

class Area(Model):
   id_area = AutoField(primary_key=True)
   nombre_area = CharField(unique=True, max_length=80)


# La estructura de la tabla Empleados deberá ser la siguiente: 
# • id int PRIMARY KEY AUTOINCREMENTAL NOT NULL 
# • nro_legajo int NOT NULL UNIQUE, 
# • dni int NOT NULL UNIQUE, 
# • nombre text NOT NULL, 
# • apellido text NOT NULL, 
# • id_area int NOT NULL 

class Empleado(Model):
    nro_legajo = IntegerField(unique=True)
    di = IntegerField(unique=True)
    nombre = CharField(max_length=50, null=False)
    apellido = CharField(max_length=50, null=False)
    area = ForeignKeyField(Area, backref='empleados')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Area: {self.area.nombre_area}"