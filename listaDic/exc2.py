# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:02:33 2021

@author: Ferlin
"""
def tradução(palavra,d1,d2,d3):
    tLatinoGregoMinusculo=dict(d1)
    tGregoMinMai=dict(d2)
    tGregoMaiNome=dict(d3)

    for letra in palavra:
        if(letra in tLatinoGregoMinusculo):
            lower=tLatinoGregoMinusculo.get(letra)
            if(lower in tGregoMinMai):
                upper=tGregoMinMai.get(lower)
                if(upper in tGregoMaiNome):
                    nome=tGregoMaiNome.get(upper)
                else:
                    print("nao tem nome")
                    return
            else:
                print("nao tem upper")
                return
            print(letra, "-- min:", lower, "mai:", upper, "nome:", nome )
        else:
            print(letra,"-- sem correspondência")
        
    return
    
tGregoMaiNome=(('Α','alfa'),('B','beta'),('Γ','gama'),('Δ','delta'),
               ('Ε','épsilon'),('Ζ','dzeta'),('Η','eta'),('Θ','teta'),
               ('Ι','iota'),('Κ','capa'),('Λ','lambda'),('M','mü'),
               ('N','nü'),('Ξ','ksi'),('Ο','ômicron'),('Π','pi'),
               ('Ρ','rô'),('Σ','sigma'),('Τ','tau'),('Υ','upsilon'),
               ('Φ','fi'),('Χ','qui'),('Ψ','psi'),('Ω','ômega'))

tLatinoGregoMinusculo = (('a','α'),('b','β'),('c','γ'),('d','δ'),
                          ('e','ε'),('z','δ'),('ê','η'),('t','θ'),
                          ('j','ι'),('k','k'),('L','λ'),('m','μ'),
                          ('n','ν'),('x','ξ'),('o','ο'),('p','π'),
                          ('r','ρ'),('s','σ'),('t','τ'),('u','υ'),
                          ('f','φ'),('qu','χ'),('ps','ψ'),('ô','ω'))
tGregoMinMai=(('α','Α'),('β','B'),('γ','Γ'),('δ','Δ'),
              ('ε','Ε'),('δ','Ζ'),('η','Η'),('θ','Θ'),
              ('ι','Ι'),('k','Κ'),('λ','Λ'),('μ','M'),
              ('ν','N'),('ξ','Ξ'),('ο','Ο'),('π','Π'),
              ('ρ','Ρ'),('σ','Σ'),('τ','Τ'),('υ','Υ'),
              ('φ','Φ'),('χ','Χ'),('ψ','Ψ'),('ω','Ω'))

tradução("pago",tLatinoGregoMinusculo,tGregoMinMai,tGregoMaiNome)

'''
Construa uma função que receba uma palavra no alfabeto latino e
as relações expressas na tuplas tGregoMaiNome, tLatinoGregoMinusculo,
e tGregoMinMai. Para cada caracter desta palavra com correspondência no alfabeto grego
 mostre-o em minúsculo, maiúsculo e nome. Quando não há correspondência,
 exibir mensagem
 Exemplo: Palavra recebida: pago
          p -- min: π   mai: p  nome:pi
          a -- min: α   mai: Α  nome:alfa
          g -- sem correspondência
          o -- min: o   mai: Ο  nome:ômicron
''' 