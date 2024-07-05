import globales
import os
import estadisticas
import ventas

def menu_general():
    while True:
        os.system("cls")
        print("== MENU ==")
        print("1. Asignar Montos aleatorios")
        print("2. Estadisticas")
        print("3. Salir programa")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar ventas aleatorias")
            ventas.precargar_precios()
        elif opcion == 2:
            print("2. Estadisticas")
            estadisticas.menu_estadisticas()
        elif opcion == 3:
            return
        input()

if __name__ == "__main__":
    menu_general()