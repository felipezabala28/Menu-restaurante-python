# Matriz del menú
# [Nombre del Producto, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rápida", 18000],
    ["Pizza", "Comida Rápida", 25000],
    ["Ensalada César", "Saludable", 16000],
    ["Jugo Natural", "Bebidas", 9000],
    ["Filete de Pollo", "Plato Fuerte", 32000],
    ["Postre de Chocolate", "Postres", 14000]
]

# Categoría objetivo y umbral
categoria_objetivo = "Comida Rápida"
umbral_precio = 20000

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base):

    # Verifica si cumple la promoción
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final

# Mostrar resultados
print("===== MENÚ DEL RESTAURANTE =====\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamado a la función
    precio_final = calcular_precio_final(categoria, precio_base)

    # Mostrar información
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", round(precio_final))
    print("-----------------------------------")