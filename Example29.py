# Ejemplo 29: Venta máxima en sucursales
# Cada sublista representa las ventas diarias de una sucursal durante una semana

ventas_semanales = [
    [150, 200, 180, 220, 250],
    [180, 190, 210, 200, 230],
    [120, 130, 110, 140, 100],
    [260, 240, 280, 270, 290]
]

venta_maxima = ventas_semanales[0][0]

for sucursal in ventas_semanales:
    for venta in sucursal:
        if venta > venta_maxima:
            venta_maxima = venta

print(f"La venta mas alta registrada fue: {venta_maxima}")