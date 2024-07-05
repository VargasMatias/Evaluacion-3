import globales
import math
import ventas
import os


def menu_estadisticas():
    while True:
        os.system("cls")
        print("== MENU ESTADISTICAS ==")
        print("1. Producto con valor mas alto")
        print("2. Producto con valor del IVA mas bajo")
        print("3. Promedio del valor de los productos")
        print("4. Media geometrica")
        print("5. Salir")

        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            print("1. Producto con valor mas alto")
            buscar_venta_mas_alta()
        elif opcion == 2:
            print("2. Producto con valor del IVA mas bajo")
            buscar_venta_mas_baja()
        elif opcion == 3:
            print("3. Promedio del valor de los productos")
            obtener_promedio_productos()
        elif opcion == 4:
            print("4. Media geometrica")
            obtener_media_geometrica()
        elif opcion == 5:
            return
        input()


            




def buscar_venta_mas_alta():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_precio'], reverse=True)

    print("| producto | total_precio |")
    for venta in ventas_ordenadas[:1]:
        print(f"{venta['nombre']} | {venta['total_precio']}")

def buscar_venta_mas_baja():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_precio'], reverse=False)

    print("| producto | total_precio |")
    for venta in ventas_ordenadas[:1]:
        print(f"{venta['nombre']} | {venta['total_precio']}")

def obtener_media_geometrica():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas[:1]:
        suma_ventas += math.log(venta['total_precio'])
        cantidad_ventas += 1

        media_geometrica = math.exp(suma_ventas / cantidad_ventas)

        print(f"La media geometrica del valor de los productos es de ${int(media_geometrica)}")


def obtener_promedio_productos():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    suma_ventas = 0
    cantidad_ventas = 0

    for venta in todas_las_ventas[:1]:
        suma_ventas += venta['total_precio']
        cantidad_ventas += 1

        promedio_productos = suma_ventas / cantidad_ventas

        print(f"El promedio del valor de los productos es de ${int(promedio_productos)}")

