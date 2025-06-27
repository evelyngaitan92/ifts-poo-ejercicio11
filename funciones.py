# El programa debe solicitar al usuario que
# ingrese por consola una de las siguientes opciones: 
# • Opcion 4 Modificar el area de un empleado en función de su número de legajo. 
# • Opcion 5 Eliminar un empleado a partir del número de legajo. 
# • Opcion 6 Finalizar. 

from modelos import Empleado, Area
from peewee import DoesNotExist, Model, SqliteDatabase
from database import db


db = SqliteDatabase('empleados.db')

class BaseModel(Model):
    class Meta:
        database = db


#crear areas 

def insertar_area(nombre_area):
    try:
        area = Area.create(nombre_area=nombre_area)
        return f" ✔️ Área '{area.nombre_area}' creada correctamente con ID {area.id_area}."
    except Exception as e:
        return f"Error al insertar área: {e}"

def listar_areas():
    try:
        print("\nÁreas disponibles:")

        areas = Area.select()
        if areas and len(areas) > 0: 
            for area in areas:
                print(f"{area.id_area} - {area.nombre_area}")
        else:
            print("No hay áreas registradas.")
    except Exception as e:
        return f"Error al listar áreas: {e}"
    
# Insertar un registro de empleado. 
     
def insertar_empleado(nro_legajo, dni, nombre, apellido, id_area):
    try:
        area = Area.get(Area.id_area == id_area)
        empleado = Empleado.create(nro_legajo=nro_legajo, dni=dni, nombre=nombre, apellido=apellido, area=area)
        return f"Empleado {empleado} insertado correctamente."
    except DoesNotExist:
        return "El área especificada no existe."
    except Exception as e:
        return f"Error al insertar empleado: {e}"
    
# Seleccionar un empleado por su número de DNI.

def seleccionar_empleado_por_dni(dni):
    try:
        empleado = Empleado.get(Empleado.dni == dni)
        return str(empleado)
    
    except DoesNotExist:
         return "Empleado no encontrado."
    
    except Exception as e:
         return f"Error al seleccionar empleado: {e}"  
    
#Seleccionar todos los empleados o los registros de la tabla. 

def seleccionar_empleados():
    try:
        empleados = Empleado.select()
        if empleados:
            return [str(empleado) for empleado in empleados]
        else:
            return "No hay empleados registrados."
    except Exception as e:
        return f"Error al seleccionar empleados: {e}"
    
# Modificar el area de un empleado en función de su número de legajo.

def modificar_area_empleado(nro_legajo, nuevo_id_area):
    try:
        empleado = Empleado.get(Empleado.nro_legajo == nro_legajo)
        nuevo_area = Area.get(Area.id_area == nuevo_id_area)
        empleado.area = nuevo_area
        empleado.save()
        return f"Área del empleado {empleado} modificada correctamente."
    except DoesNotExist:
        return "Empleado o área no encontrado."
    except Exception as e:
        return f"Error al modificar área de empleado: {e}"
    
#Eliminar un empleado a partir del número de legajo.

def eliminar_empleado(nro_legajo):
    try:
        empleado = Empleado.get(Empleado.nro_legajo == nro_legajo)
        empleado.delete_instance()
        return f"Empleado {empleado} eliminado correctamente."
    except DoesNotExist:
        return "Empleado no encontrado."
    except Exception as e:
        return f"Error al eliminar empleado: {e}"
    