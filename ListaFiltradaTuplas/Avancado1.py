# Exercício Difícil 1 — Compressão de texto (Run-Length Encoding)

# Escreva uma função chamada comprimir_texto(texto) que:
# Receba uma string.
# Analise a sequência de caracteres da string.
# Agrupe caracteres consecutivos iguais.

# Retorne uma tupla de tuplas, onde cada tupla contém:
# (caractere, quantidade_de_repetições_consecutivas)

# Exemplo

# Entrada:
# "aaabbc"

# Saída:
# (('a',3), ('b',2), ('c',1))

# Outro exemplo:

# Entrada:
# "hellooo!!"

# Saída:
# (('h',1), ('e',1), ('l',2), ('o',3), ('!',2))

def comprimir_texto(texto):
    listaString=[]
    listaFrequencia=[]
    listaRetorno=[]
    for caracter in texto:
        if(caracter in listaString):
            listaFrequencia[listaString.index(caracter)]+=1
        else:
            listaString.append(caracter)
            listaFrequencia.append(1)
            
    for i in range(len(listaString)):
        listaRetorno.append((listaString[i],listaFrequencia[i]))
    return tuple(listaRetorno)

texto="aaabbc"
print(comprimir_texto(texto))