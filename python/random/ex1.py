""" 
Crie uma função chamada gerar_uuid que gera um UUID personalizado com base nos seguintes critérios:

    O UUID deve ter um comprimento de 12 caracteres.
    O UUID deve ser composto apenas por letras maiúsculas (A-Z) e dígitos (0-9).

Gere uma lista de 5 UUIDs utilizando a função gerar_uuid.

Imprima a lista de UUIDs gerados.
"""
import random
from string import ascii_uppercase as l, digits as d


def gerar_uuid(qtd: int):
    list = ["".join(random.choices(l + d, k=12)) for _ in range(0, qtd)]
    return list


print(gerar_uuid(5))
