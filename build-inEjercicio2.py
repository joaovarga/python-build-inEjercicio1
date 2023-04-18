from functools import reduce

# Creamos la lista de números del 0 al 99 utilizando una comprensión de lista
numeros_lista = [num for num in range(100)]

# Utilizamos la misma función para obtener los números pares e impares
def obtener_lista_numeros(n, condicion):
    return list(filter(condicion, n))

# Creamos las listas de pares e impares utilizando la función genérica
numeros_pares = obtener_lista_numeros(numeros_lista, lambda x: x % 2 == 0)
numeros_impares = obtener_lista_numeros(numeros_lista, lambda x: x % 2 != 0)

# Sumamos los elementos de cada lista utilizando la función reduce
suma_pares = reduce(lambda x, y: x + y, numeros_pares)
suma_impares = reduce(lambda x, y: x + y, numeros_impares)

# Imprimimos las listas y la suma de los elementos
print("Números pares:", numeros_pares)
print("Números impares:", numeros_impares)
print("Suma de números pares:", suma_pares)
print("Suma de números impares:", suma_impares)
