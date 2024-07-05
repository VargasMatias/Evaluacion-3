import globales
import random

def precargar_precios():
    ventas = globales.leer_archivo_json('ventas.json')
    productos = globales.leer_archivo_json('productos.json')

    for i in range(15):
        producto = random.choice(productos)

        nombre = producto['nombre']
        total_precio = random.randint(20, 100) *100
        iva = total_precio * 0.19
        

        nuevo_precio = {
            "nombre" : nombre,
            "total_precio" : total_precio,
            "iva" : iva,
            
        }
        ventas.append(nuevo_precio)

    globales.guardar_archivo_json('ventas.json', ventas)
    input("Precios cargados")


