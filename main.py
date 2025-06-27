from funciones import (
    insertar_empleado,
    seleccionar_empleados,
    seleccionar_empleado_por_dni,
    modificar_area_empleado,
    eliminar_empleado,
    insertar_area,          # 🔽 NUEVO
    listar_areas            # 🔽 NUEVO
)

from modelos import db, Area, Empleado
from peewee import SqliteDatabase

db = SqliteDatabase('empleados.db')

def crear_tablas():
    db.connect()
    db.create_tables([Area, Empleado])
    print("✔️ Tablas creadas o verificadas correctamente.")

def mostrar_menu():
    print("\n--- Menú de Gestión de Empleados ---")
    print("0. Insertar un área")  
    print("1. Insertar un empleado")
    print("2. Buscar empleado por DNI")
    print("3. Listar todos los empleados")
    print("4. Modificar área de un empleado por legajo")
    print("5. Eliminar un empleado por legajo")
    print("6. Salir")

def main():
    crear_tablas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-6): ")

        if opcion == '0':
            nombre_area = input("Ingrese el nombre del área: ")
            print(insertar_area(nombre_area))

        elif opcion == '1':
            print("\nInsertar nuevo Empleado:")
            
            nro_legajo = int(input("Número de legajo: "))
            dni = int(input("DNI: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")

            listar_areas()

            id_area = int(input("ID del área: "))
            print(insertar_empleado(nro_legajo, dni, nombre, apellido, id_area))

        elif opcion == '2':
            try:
                dni = int(input("Ingrese el DNI del empleado a buscar: "))
                resultado = seleccionar_empleado_por_dni(dni)
                print(resultado)
            except ValueError: print("❌ El DNI debe ser un número.")

        elif opcion == '3':
            print("\nLista de Empleados:")
            resultado = seleccionar_empleados()
            if isinstance(resultado, list):
                for emp in resultado:
                    print(emp)
            else:
                print(resultado)

        elif opcion == '4':
            nro_legajo = int(input("Número de legajo del empleado a modificar: "))

            listar_areas()
            nuevo_id_area = int(input("Nuevo ID del área: "))
            print(modificar_area_empleado(nro_legajo, nuevo_id_area))

        elif opcion == '5':
            nro_legajo = int(input("Número de legajo del empleado a eliminar: "))
            print(eliminar_empleado(nro_legajo, nombre))

        elif opcion == '6':
            print("Saliendo del programa. 👋")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
