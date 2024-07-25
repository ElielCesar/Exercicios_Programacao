""" 
Use a função any() para verificar se há pelo menos uma string vazia na lista palavras.

Imprima uma mensagem indicando se há ou não strings vazias na lista.

"""
palavras = ["casa", "", "carro", "bicicleta", "", "avião"]

if any(len(p)== 0 for p in palavras):
    print("Existe strings vazias")

