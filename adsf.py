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
        s = False
        while s == False:
            id = int(input(f"Ingrese el id del empleado {v}: "))
            if id in empleados:
                print("ID invalido, ingreselo de nuevo")
            else:
                s = True
        nombre = input("Ingrese el nombre: ")
        s = False
        while s == False:
            edad = int(input("Ingrese la edad: "))
            if edad > 18 and edad < 80:
                s = True
            else:
                print("Edad invalida")
        departamento = input("Ingrese el departamento: ")
        s = False
        while s == False:
            sueldo_mensual = float(input("Ingrese su sueldo mensual: "))
            if sueldo_mensual > 0:
                s = True
            else:
                print("Sueldo mensual invalido.")
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
            s = False
            while s == False:
                bonifiacion = float(input("Ingrese la cantidad de la bonificacion: "))
                if bonifiacion > 0:
                    s = True
                else:
                    print("Bonificacion invalida")
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
        print("No hay empleados registrados")

def buscar_empleados():
    if len(empleados) > 0:
        print("===Buscar empleado===")
        buscar = int(input("Ingrese el ID del empleado: "))
        if buscar in empleados:
            print(f"Nombre: {empleados[buscar]['nombre']}, Edad: {empleados[buscar]['edad']}. Departamento: {empleados[buscar]['departamento']}, Sueldo mensual: {empleados[buscar]['sueldo_mensual']}")
            print("Bonificaciones:")
            for motivo, bonificaciones in empleados[buscar]['bonificaciones'].items():
                print(f"Motivo: {motivo}")
                print(f"Bonificacion: {bonificaciones['bonificacion']}")
    else:
        print("No hay empleados registrados")

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
            buscar_empleados()
        case 4:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")