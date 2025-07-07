import time
import tracemalloc
from mergeSort import merge_sort

def busqueda_secuencial(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1

# Función para medir Merge Sort
def medir_merge_sort(arreglo):
    arr = arreglo.copy()  # Para no modificar el original

    tracemalloc.start()
    inicio = time.time()
    merge_sort(arr, 0, len(arr)-1)
    tiempo = time.time() - inicio
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Merge Sort ({len(arr)} elementos):")
    print(f"  Tiempo: {tiempo * 1_000:.4f} milisegundos")
    print(f"  Memoria: {memoria_pico / 1024:.4f} KB")
    return tiempo, memoria_pico, arr # Devolver también el arreglo ordenado

# Función para medir búsqueda
def medir_busqueda(arreglo, valor):
    tracemalloc.start()
    inicio = time.time()
    resultado = busqueda_secuencial(arreglo, valor)
    tiempo = time.time() - inicio
    memoria_actual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Búsqueda ({len(arreglo)} elementos):")
    print(f"  Tiempo: {tiempo * 1_000:.4f} milisegundos → Índice: {resultado}")
    print(f"  Memoria: {memoria_pico / 1024:.4f} KB")
    return tiempo, memoria_pico