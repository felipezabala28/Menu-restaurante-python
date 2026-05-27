# Nombre del estudiante: Andrés Felipe Zabala Bello
# Grupo: 213022B_2201
# Programa: FUNDAMENTOS DE PROGRAMACIÓN
# Código fuente: Autoría propia

# Entrada de datos
residentes = int(input("Ingrese la cantidad de residentes: "))
cuota = float(input("Ingrese el valor de la cuota mensual: "))

# Variables contadoras
al_dia = 0
morosos = 0
total_deuda = 0

# Proceso repetitivo
for i in range(residentes):
    print("\nVecino", i + 1)
    pago = input("¿Pagó la cuota? (si/no): ").lower()
    
    if pago == "si":
        print("Estado: Al día")
        al_dia += 1
    else:
        print("Estado: Moroso")
        morosos += 1
        total_deuda += cuota

# Resultados
print("\n--- RESULTADOS ---")
print("Vecinos al día:", al_dia)
print("Vecinos morosos:", morosos)
print("Total adeudado:", total_deuda)