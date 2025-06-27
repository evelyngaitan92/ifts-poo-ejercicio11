from peewee import SqliteDatabase
from modelos import Area, Empleado 

db = SqliteDatabase('empleados.db')

# La aplicación debe permitir crear las tablas utilizando el método create_tables() 
# del módulo  peewee. 

def create_tables():
    with db:
        db.create_tables([Area, Empleado])

