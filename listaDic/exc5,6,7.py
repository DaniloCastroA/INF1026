# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 00:17:11 2024

@author: Ferlin
"""
'''
5.	Considere o dicionário com as despesas da filial1 e outro com as 
despesas da filial2 de uma empresa.
 Estes dicionários tem como chave a despesa e como valor o montante 
 gasto pela filial com a respectiva despesa. 
 Construa a função  combinar_dicionarios que receba uma tupla com as
 despesas a serem analisadas e  os dois dicionários de despesas e 
 retorne um novo dicionário contendo as chaves da tupla (despesas) e 
 os valores correspondentes encontrados nos dicionários. 
 Se uma chave estiver presente em ambos os dicionários, 
 o valor no novo dicionário deve ser a soma dos valores 
 correspondentes. . (SIMPLIFICANDO COM O MÉTODO GET)
 '''

def combinar_dicionarios(tupla,dic1,dic2):
    dicComb={}
    for elemento in tupla:
        if(elemento in dic1 and elemento in dic2):
            dicComb[elemento]=dic1.get(elemento)+dic2.get(elemento)
        elif(elemento in dic1):
            dicComb[elemento]=dic1.get(elemento)
        elif(elemento in dic2):
            dicComb[elemento]=dic2.get(elemento)
    return dicComb

# Exemplo de uso
print("\n\n==========> Ex 5 ")
tupla = ('aluguel', 'luz', 'agua', 'condominio','internet','telefone')
dFililal_1 = {'aluguel': 1000, 'luz': 250, 'agua': 350,'limpeza': 200, 'material': 400, 'condominio': 1500,'internet':500}
dFililal_2 = {'luz': 250, 'água': 350,'limpeza': 200, 'material': 400, 'telefone':500, 'internet':500}

novo_dicionario = combinar_dicionarios(tupla, dFililal_1,dFililal_2)
print(novo_dicionario)


'''
6.	Suponha que você tenha uma tupla contendo chaves que correspondem 
a possíveis chaves em dois dicionários diferentes.
 Construa uma função que receba a tupla e os dois dicionários e 
 retorne um novo dicionário que combine os valores dos dois 
 dicionários com base nas chaves da tupla., isto é: 
     chave: item da tupla  e  
     valor: tupla com os valores dos dicionários cujas chaves equivalem ao valor da tupla. Caso a chave esteja apenas em um dicionário, não deve ser incluída no novo dicionário. (SIMPLIFICANDO COM O MÉTODO GET)
'''

print("\n\n==========> Ex 6 ")

def ex6acombinar_dicionarios (tuplaDTuplas,dic1,dic2):
    combDic={}
    for elemento1,elemento2 in tuplaDTuplas:
        if(elemento1 in dic1 and elemento2 in dic2):
            combDic[elemento1,elemento2]=(dic1.get(elemento1),dic2.get(elemento2))
    return combDic


# Exemplo de uso
tupla_de_tuplas = (('a', 'b'), ('c', 'd'), ('e', 'f'),('e','k'),('w','f'),('9','7'))
dicionario1 = {'a': 1, 'c': 3, 'e': 5}
dicionario2 = {'b': 'x', 'd': 'y', 'f': 'z'}
novo_dicionario = ex6acombinar_dicionarios(tupla_de_tuplas, dicionario1, dicionario2)
print(novo_dicionario)

'''
7.	Construa uma função que recebe uma tupla de tuplas,
 onde cada tupla interna contém duas chaves e dois dicionários. 
 Esta função deve retornar um novo dicionário com as chaves da tupla
 de tuplas e os valores correspondentes encontrados nos dois 
 dicionários. 
 Se uma chave estiver presente em ambos os dicionários, 
 o valor no novo dicionário deve ser uma lista contendo os valores 
 correspondentes. Se uma chave estiver presente em apenas um dos 
 dicionários, a função adiciona apenas o valor correspondente desse 
 dicionário ao novo dicionário. (SIMPLIFICANDO COM O MÉTODO GET)
 '''
print("\n\n==========> Ex7 ")

def ex7bcombinar_dicionarios(tupla_de_tuplas, dicionario1, dicionario2):
    newDic={}
    for elemento1, elemento2 in tupla_de_tuplas:
        if(elemento1 in dicionario1 and elemento2 in dicionario2):
            newDic[elemento1,elemento2]=list((dicionario1.get(elemento1),dicionario2.get(elemento2)))
        elif(elemento1 in dicionario1):
            newDic[elemento1]=dicionario1.get(elemento1)
        elif(elemento2 in dicionario2):
            newDic[elemento2]=dicionario2.get(elemento2)
    return newDic



# Exemplo de uso
tupla_de_tuplas = (('a', 'b'), ('c', 'd'), ('e', 'f'),('e','k'),('w','f'),('9','7'))
dicionario1 = {'a': 1, 'c': 3, 'e': 5}

novo_dicionario = ex7bcombinar_dicionarios(tupla_de_tuplas, dicionario1, dicionario2)
print(novo_dicionario)
# dicionario2 = {'b': 'x', 'd': 'y', 'f': 'z'}