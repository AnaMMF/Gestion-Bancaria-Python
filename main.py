import person

print("\n¡BIENVENIDO A BANCO ZETA!\nEscoge una de las siguiente opciones:")

while True:
    print("1. Abrir una nueva cuenta.")
    print("2. Ver un listado de las cuentas disponibles")
    print("3. Obtener los datos de una cuenta concreta.")
    print("4. Realizar un ingreso en una cuenta.")
    print("5. Retirar efectivo de una cuenta.")
    print("6. Consultar el saldo actual de una cuenta.")
    print("7. Salir de la aplicación.")

    print("\n")
    option=int(input())
    print("\n")

    match option:
        case 1:
            name=input()
            lastname=input()
            dni=input()
            person.person(name, lastname, dni)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Cierre del programa. Hasta pronto.")
            break
        case _:
            print("Opción incorrecta. Introduzca un número del 1 al 7.")