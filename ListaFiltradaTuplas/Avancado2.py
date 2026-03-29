# Exercício Difícil 2 — Análise de apostas da Mega-Sena

# As apostas de um sorteio da Mega-Sena estão armazenadas em duas tuplas paralelas:
# A primeira contém os nomes dos jogadores.
# A segunda contém as apostas correspondentes (tuplas de números).
# Cada aposta contém 6 números, mas não necessariamente está ordenada.

# Exemplo:
# tNomes = ('Kaka', 'Keko', 'Kiko', 'Kako', 'Kiko', 'Kaka', 'Keko', 'Kiko')
# tApostas = (
#  (1,2,6,44,49,59),
#  (1,2,6,37,18,58),
#  (1,2,40,37,51,58),
#  (6,3,18,49,45,57),
#  (6,2,25,37,38,39,42,54),
#  (51,18,37,40,44,4),
#  (6,25,40,41,51,52,57),
#  (1,2,6,37,49,59)
# )
# O resultado do sorteio é representado por uma tupla de 6 números sorteados.

# Escreva uma função chamada maiorNumeroAcertos(tJogos, resultado) que:

# Receba uma tupla de jogos no formato:
# (nome, aposta)
# Compare cada aposta com o resultado do sorteio.
# Conte quantos números cada aposta acertou.

# Determine:
# o maior número de acertos obtido em uma aposta
# os nomes dos jogadores que tiveram essa quantidade de acertos (sem repetição)

# A função deve retornar uma tupla contendo:
# (maior_numero_de_acertos, (nomes_dos_jogadores))

def maiorNumeroAcertos(tJogos, resultado):
    contador=0
    maiorAcerto=-1
    
    for jogos in tJogos:
        nome=jogos[0]
        numeros=jogos[1]
        for numero in numeros:
            for indice in range(len(resultado)):
                if(numero==resultado[indice]):
                    contador=contador+1
       
        if(maiorAcerto<contador):
            maiorAcerto=contador
            listaNome=[nome]
        if(maiorAcerto==contador):
            if(nome not in listaNome):
                listaNome.append(nome)
            
        contador=0
    return (maiorAcerto,tuple(listaNome))

tupla= ( ('Kaka',(1,2,6,44,49,59)),
 ('Keko',(1,2,6,37,18,58)),
 ('Kiko',(1,2,40,37,51,58)),
 ('Kako',(6,3,18,49,45,57)),
 ('Kaka',(6,2,25,37,38,39,42,54)),
 ('Keko',(51,18,37,40,44,4)),
 ('Kiko',(6,25,40,41,51,52,57)))
print(maiorNumeroAcertos(tupla, (6,3,1,49,45,57)))