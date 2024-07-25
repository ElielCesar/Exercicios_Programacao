"""
Use a função zip() para combinar as listas nomes e idades em uma lista de tuplas,
onde cada tupla contém um nome e a idade correspondente.

Percorra a lista de tuplas resultante e imprima o nome e a idade de cada pessoa no formato:
"Nome: {nome}, Idade: {idade}".

"""

nomes = ["Ana", "Carlos", "Beatriz", "João", "Maria"]
idades = [25, 30, 22, 28, 24]
lista = list(zip(nomes, idades))

for nome, idade in lista:
    print(f"Nome: {nome}, Idade: {idade}")