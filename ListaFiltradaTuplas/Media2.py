# Exercício Médio 2 — Ranking de vendas

# Considere uma lista de vendedores, onde cada elemento é uma tupla no formato:
# (nome, total_vendas)

# Escreva uma função chamada melhor_vendedor(vendas) que:
# Receba uma lista de tuplas com os vendedores e seus totais de vendas.
# Determine qual vendedor possui o maior valor de vendas.
# Retorne o nome do vendedor com maior total de vendas.

# Exemplo de entrada
# [("Carlos", 1500), ("Ana", 2300), ("João", 1800)]
# Exemplo de saída
# Ana

def melhor_vendedor(vendas):
    maiorValor=0
    for venda in vendas:
        if(maiorValor<venda[1]):
            maiorValor=venda[1]
            nomeVendedor=venda[0]
    return nomeVendedor

listaDeTuplas=[("Carlos", 1500), ("Ana", 2300), ("João", 1800)]
print(melhor_vendedor(listaDeTuplas))