from interfaz.menu import menu
from persistencia.persistencia import *

#Programa
archivoClientes = "clientes.dat"
archivoProductos = "productos.dat"
archivoVentas = "ventas.dat"


while True:
    op = menu()
    match op:
        case 1:
            print("\nConsulta de facturas \n")
            imprimirFactura(archivoVentas, archivoClientes, archivoProductos)
        case 2:
            print("\nResumen de facturas\n")
            resumenCliente(archivoVentas, archivoClientes, archivoProductos)
        case 3:
            print("Funcion disponible en la version alfa")
        case 4:
            print("Funcion disponible en la version alfa")
        case 5:
            print("\Gracias por usar el software\n")
            break