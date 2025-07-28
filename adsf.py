#Desarrolle un programa en Python que permita registrar
# empleados de una empresa. Cada empleado se identificará
# por su ID numérico único, y se deben guardar los siguientes datos:
#Nombre, Edad, Departamento, Sueldo mensual (mayor a 0), bonificaciones
empleados = {}

def registrar_empleados():
    nombre = input("Ingrese el nombre: ")
    edad = int

opcion = 0
a = False
while a == False:
    print("===Menu empleados===")
    print("1. Registrar empleados")
    print("2. Mostrar todos los empleados y sus bonificaciones")
    print("3. Buscar empleado por ID")
    print("4 Salir")
    opcion = int(input("Elija una opcion: "))
    match opcion:
        case 1:
            print("adsf")
        case 2:
            print("asdf")
        case 3:
            print("asdf")
        case 4:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")