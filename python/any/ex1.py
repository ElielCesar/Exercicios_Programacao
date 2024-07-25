""" 
Use a função any() para verificar se há pelo menos um número positivo na lista numeros.

Imprima uma mensagem indicando se há ou não números positivos na lista.
"""
numeros = [10, -4, 0, -7, 5, -3]
result = any(x > 0 for x in numeros)
print(result)