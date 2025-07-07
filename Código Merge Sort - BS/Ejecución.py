import numpy as np
from medirMerge import medir_busqueda, medir_merge_sort

try:
    num_elementos = int(input("Ingrese el número de elementos para el arreglo: "))
except ValueError:
    print("Entrada no válida. Usando 1000 elementos por defecto.")
    num_elementos = 1000

# --- Generación de Arreglos para Pruebas ---
# Arreglo para caso promedio (aleatorio)
arr_aleatorio = np.random.randint(0, num_elementos * 10, size=num_elementos).tolist()
# Arreglo para mejor caso de Merge Sort (ya ordenado)
arr_ordenado = sorted(arr_aleatorio)
# Arreglo para peor caso de Merge Sort (orden inverso)
arr_inverso = sorted(arr_aleatorio, reverse=True)

print(f"\nArreglo base generado con {num_elementos} elementos.")
print("-" * 40)

# --- Análisis de Búsqueda Secuencial ---
print("\n--- Análisis de Búsqueda Secuencial ---")

print("\n1. Mejor Caso (Elemento en la primera posición)")
valor_mejor_caso = arr_aleatorio[0]
print(f"Buscando el valor: {valor_mejor_caso}")
medir_busqueda(arr_aleatorio, valor_mejor_caso)

print("\n2. Caso Promedio (Elemento en posición aleatoria)")
valor_caso_promedio = arr_aleatorio[np.random.randint(0, num_elementos)]
print(f"Buscando el valor: {valor_caso_promedio}")
medir_busqueda(arr_aleatorio, valor_caso_promedio)

print("\n3. Peor Caso (Elemento no existe)")
valor_peor_caso = -1  
print(f"Buscando el valor: {valor_peor_caso}")
medir_busqueda(arr_aleatorio, valor_peor_caso)

print("-" * 40)

# --- Análisis de Merge Sort ---
print("\n--- Análisis de Merge Sort ---")

# Caso Promedio: Arreglo aleatorio
print("\n1. Caso Promedio (Arreglo aleatorio)")
medir_merge_sort(arr_aleatorio)

# Mejor Caso: Arreglo ya ordenado
print("\n2. Mejor Caso (Arreglo ya ordenado)")
medir_merge_sort(arr_ordenado)

# Peor Caso: Arreglo en orden inverso
print("\n3. Peor Caso (Arreglo en orden inverso)")
medir_merge_sort(arr_inverso)

print("-" * 40)

