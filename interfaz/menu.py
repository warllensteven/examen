def menu():
    while True:
        print("** Billify **")
        print("1. Consultar factura")
        print("2. Resumen de cliente")
        print("3. Diagrama de barras(indicativo de ventas al año)")
        print("4. Lista de productos comunes en dos usuarios")
        print("5. Salir")

        print(">>> Opcion? ", end="")
        try:
            opcion = int(input())
            if opcion <1 or opcion > 4:
                print("Error. Opcion no valida...")
                input("Presione cualquier tecla  para volver al menu")
                continue
            return opcion
        except ValueError:
            print("Error. Opcion no valida...")
            input("Presione cualquier tecla para volver al menu") 