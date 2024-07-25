""" 
Use list comprehension para criar uma nova lista chamada quadrados_pares que contém os quadrados dos números pares da lista numeros.

Use list comprehension para criar uma nova lista chamada triplo_impares que contém o triplo dos números ímpares da lista numeros.

Imprima as listas quadrados_pares e triplo_impares.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados_pares = [x**2 for x in numeros if x % 2 == 0]
triplo_impares = [x*3 for x in numeros if x % 2 != 0]

print(quadrados_pares)
print(triplo_impares)