# El programa debe solicitar al usuario que
# ingrese por consola una de las siguientes opciones: 
# • Opcion 1 Insertar un registro de empleado. 
# • Opcion 2 Seleccionar un registro de empleado a partir de su número DNI. 
# • Opcion 3 Seleccionar todos los empleados o los registros de la tabla. 
# • Opcion 4 Modificar el area de un empleado en función de su número de legajo. 
# • Opcion 5 Eliminar un empleado a partir del número de legajo. 
# • Opcion 6 Finalizar. 

from modelos import Empleado, Area
from peewee import DoesNotExist

# Funciones empleados

def insertar_empleado(nro_legajo, dni, nombre, apellido, id_area):
    try:
        area = Area.get(Area.id_area == id_area)
        empleado = Empleado.create(nro_legajo=nro_legajo, dni=dni, nombre=nombre, apellido=apellido, area=area)
        return f"Empleado {empleado} insertado correctamente."
    except DoesNotExist:
        return "El área especificada no existe."
    except Exception as e:
        return f"Error al insertar empleado: {e}"
    
# def seleccionar_empleado_por_dni(dni):
#     try:
#         empleado = Empleado.get(Empleado.dni == dni)
#         return str(empleado)
#     except DoesNotExist:
#         return "Empleado no encontrado."
#     except Exception as e:
#         return f"Error al seleccionar empleado: {e}"  