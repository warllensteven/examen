archivoClientes = "clientes.dat"
archivoProductos = "productos.dat"
archivoVentas = "ventas.dat"

def imprimirFactura(archivoVentas,archivoClientes,archivoProductos):
    fdVentas = open(archivoVentas, "r")
    fdClientes = open(archivoClientes, "r")
    fdProductos = open(archivoProductos, "r")
    factura = input("Ingrese el codigo de la factura que desea consultar: ")

    for linea in fdVentas:
        v = linea.split(";")
        if v[0] == factura:
            for linea in fdClientes:
                c = linea.split(";")
                nomCliente = c[1]
                total = int(v[8])
                fac = int(v[7])
                iva = total -fac
                if v[4] == c[0]:
                    cliente = c[0]
                    for linea in fdProductos:
                        p = linea.split(";")
                        if v[5] == p[0]:
                            producto = p[0]
                            print("Factura encontrada")
                            print("")
                            print(f"Factura {v[0]}")
                            print(f"Fecha: {v[3]}/{v[2]}/{v[1]}")
                            print(f"Codigo del ciente: {cliente}")
                            print(f"Nombre del ciente: {nomCliente}")
                            print(f"Info Prod: {producto}")
                            print(f"Unidades prod: {v[6]}")
                            print(f"Valor factutra: {v[7]}")
                            print(f"Valor iva: ", iva)
                            print(f"Valor total: {v[8]}")



def resumenCliente(archivoVentas, archivoClientes, archivoProductos):
    fdVentas = open(archivoVentas, "r")
    fdClientes = open(archivoClientes, "r")
    fdProductos = open(archivoProductos, "r")
    cod = input("Ingrese el codigo del cliente: ")
    lstFact = []


    for linea in fdClientes:
        c = linea.split(";")
        if c[0] == cod:
            cliente = c[0]
            nomCliente = c[1]
            mes = input("Ingrese el mes que desea el resumen: ")
            for linea in fdVentas:
                v = linea.split(";")
                if v[2] == mes and cod == v[4]:
                    lstFact.append(v[0])
                    total = int(v[8])
                    fac = int(v[7])
                    iva = total -fac
                    print("Resumen")
                    print("")
                    print(f"Codigo del cliente: {cliente}")
                    print(f"Nombre del cliente: {nomCliente}")
                    print(f"mes: {v[2]}")
                    for i in range(len(lstFact)):
                        print(f"Factura: {lstFact[i]}")
                        print(f"Valor factutra: {v[7]}")
                        print(f"Valor iva: ", iva)
                        print(f"Valor total: {v[8]}")
            

# for linea in fdProductos:
#                         p = linea.split(";")
#                         if v[5] == p[0]:
#                             producto = p[0]
#                             
    


# imprimirFactura(archivoVentas,archivoClientes,archivoProductos)

# if v[0] == factura:
            
#                         # for linea in fdClientes:
#                         #     c = linea.split(";")
#                         #     for linea in fdProductos:
#                         #         p = linea.split(";")
#         else:
#             print("Factura no encontrada")