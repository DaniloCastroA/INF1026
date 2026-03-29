# Operações matemáticas múltiplas

# Crie uma função:
# def operacoes(a, b):

# que receba dois números e retorne uma tupla com:
# soma
# subtração
# multiplicação
# divisão

# Exemplo esperado:
# operacoes(8,4)
# (12, 4, 32, 2)

def operacoes(a, b):
    soma=a+b
    subtracao=a-b
    multiplicacao=a*b
    divisao=a/b
    tupla=(soma,subtracao,multiplicacao,divisao)
    return tupla
print(operacoes(8,4))