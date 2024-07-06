import globales
import math

def buscar_ventas_altas():
    todas_las_ventas = globales.leer_archivo_json('ventas.json')

    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['total_venta'],reverse=True)

    print("| id venta | empleado |total venta | propina")
    print("--------------------------------------------")
    for venta in ventas_ordenadas[:3]:
        print(f"|{venta['id_venta'] } | {venta['id_empleado']}")