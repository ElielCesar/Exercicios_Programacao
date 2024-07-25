""" 
Crie uma classe chamada Aluno que tenha os seguintes atributos:

    nome (string)
    idade (inteiro)
    nota (float)

Implemente o método __init__ para inicializar os atributos da classe.

Crie uma lista de objetos Aluno com pelo menos 5 alunos diferentes.

Use a função sorted() para ordenar a lista de alunos:

    Por nome em ordem alfabética.
    Por idade em ordem crescente.
    Por nota em ordem decrescente.
"""
class Aluno:
    def __init__(self, nome: str, idade: int, nota: float):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        
    def __repr__(self):
        return f"Nome:{self.nome}, Idade:{self.idade}, Nota:{self.nota}"
    
a1 = Aluno("Maria", 18, 8)
a2 = Aluno("Pedro", 21, 9)
a3 = Aluno("Alberto", 17, 8)
a4 = Aluno("João", 18, 7)
a5 = Aluno("Pedro", 21, 6)

queryset = [a1, a2, a3, a4, a5]

lista_ordenada = sorted(queryset, key=lambda x: (x.nome, x.idade, -x.nota))
for i in lista_ordenada:
    print(i)