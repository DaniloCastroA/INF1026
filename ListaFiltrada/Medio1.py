# Exercício Médio 1 — Classificação de notas de alunos

# Considere uma lista de alunos onde cada elemento é uma tupla no formato:
# (nome, nota1, nota2, nota3)

# Escreva uma função chamada classificar_alunos(lista_alunos) que:
# Receba uma lista de tuplas contendo os dados dos alunos.
# Calcule a média das três notas de cada aluno.

# Determine o status do aluno:
# "Aprovado" se a média for maior ou igual a 6.
# "Reprovado" caso contrário.

# Retorne uma tupla de tuplas, onde cada elemento contém:
# (nome, média, status)
# Exemplo de entrada
# [
#  ("Ana", 7.0, 6.5, 8.0),
#  ("João", 5.0, 4.5, 6.0),
#  ("Maria", 9.0, 8.5, 9.5)
# ]
# Exemplo de saída
# (
#  ("Ana", 7.16, "Aprovado"),
#  ("João", 5.16, "Reprovado"),
#  ("Maria", 9.0, "Aprovado")
# )

def classificar_alunos(lista_alunos):
    lista=[]
    media=0
    contador=0

    for element in lista_alunos:
        

        for elementT in element:
            if(type(elementT)==str):
                nome=elementT
            elif(type(elementT)==float):
                media=media+elementT
                contador=contador+1
                

        if(contador!=0):
            print(contador)
            media=media/contador
            contador=0

        if(media>6):
            situacao="aprovado"
        else:
            situacao="reprovado"
        tuplaFilho=(nome,media,situacao)
        media=0
        lista.append(tuplaFilho)
    return tuple(lista)


lista=[
("Ana", 7.0, 6.5, 8.0),
("João", 5.0, 4.5, 6.0),
("Maria", 9.0, 8.5, 9.5)
]


print(classificar_alunos(lista))

