import timeit
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def busqueda_binaria(arr, objetivo):
    inicio = 0
    fin = len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return True
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

codigos = [random.randint(0, 999) for _ in range(150)]

print("\nLista desordenada:")
print(codigos)

inicio_ordenamiento = timeit.default_timer()
codigos_ordenados = bubble_sort(codigos.copy())
fin_ordenamiento = timeit.default_timer()
tiempo_ordenamiento = fin_ordenamiento - inicio_ordenamiento

print("\nLista ordenada:")
print(codigos_ordenados)
print(f"Tiempo de ordenamiento (Bubble Sort): {tiempo_ordenamiento:.8f} segundos\n")

while True:
    entrada = input("Ingrese el código de producto a buscar (o escriba 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Gracias por usar el sistema.")
        break

    if not entrada.isdigit():
        print("Por favor, ingrese un número válido.\n")
        continue

    codigo_a_buscar = int(entrada)

    inicio_busqueda = timeit.default_timer()
    encontrado = busqueda_binaria(codigos_ordenados, codigo_a_buscar)
    fin_busqueda = timeit.default_timer()
    tiempo_busqueda = fin_busqueda - inicio_busqueda

    print(f"¿El código {codigo_a_buscar} fue encontrado?: {'Sí' if encontrado else 'No'}")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.8f} segundos\n")
