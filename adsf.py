#Desarrolle un programa en Python que permita registrar
# empleados de una empresa. Cada empleado se identificará
# por su ID numérico único, y se deben guardar los siguientes datos:
#Nombre, Edad, Departamento, Sueldo mensual (mayor a 0), bonificaciones
empleados = {}

def registrar_empleados():
    v = 0
    cantidad_empleados = int(input("Ingrese la cantidad de empleados que desea registrar: "))
    for i in range(cantidad_empleados):
        v += 1
        id = int(input(f"Ingrese el id del empleado {v}: "))
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        departamento = input("Ingrese el departamento: ")
        sueldo_mensual = float(input("Ingrese su sueldo mensual: "))
        empleados[id] = {
            "nombre": nombre,
            "edad": edad,
            "departamento": departamento,
            "sueldo_mensual": sueldo_mensual,
            "bonificaciones": {}
        }
        cantidad_bonificaciones = int(input("\nCuantas bonificaciones tendra: "))
        for i in range(cantidad_bonificaciones):
            motivo = input("Ingrese el motivo de la bonificacion: ")
            bonifiacion = float(input("Ingrese la cantidad de la bonificacion: "))
            empleados[id]["bonificaciones"][motivo] = {
                "bonificacion": bonifiacion
            }

    print("\nSe ha registrado al empleado")

def mostrar_empleados_bonificaciones():
    print("\n===Empleados registrados===")
    if len(empleados) > 0:
        for i in empleados:
            print(f"\nNombre: {empleados[i]['nombre']}, ID: {i}, Edad: {empleados[i]['edad']}, Departamento: {empleados[i]['departamento']}, Sueldo mensual: {empleados[i]['sueldo_mensual']}")
            print("Bonificaciones: ")
            for bonificaciones in empleados[i]['bonificaciones']:
                bonificacion = empleados[i]['bonificaciones'][bonificaciones]['bonificacion']
                print(f"Motivo: {bonificaciones}")
                print(f"Bonificacion: {bonificacion}")
    else:
        print("No hay estudiantes registrados")

opcion = 0
a = False
while a == False:
    print("\n===Menu empleados===")
    print("1. Registrar empleados")
    print("2. Mostrar todos los empleados y sus bonificaciones")
    print("3. Buscar empleado por ID")
    print("4 Salir")
    opcion = int(input("Elija una opcion: "))
    match opcion:
        case 1:
            registrar_empleados()
        case 2:
            mostrar_empleados_bonificaciones()
        case 3:
            print("asdf")
        case 4:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")