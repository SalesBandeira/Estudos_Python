# Faça um programa para imprimir:

from ast import Return
from calendar import c

from pandas import concat


def imprimir(n):
    for num in range(1,n+1):
        print(n)

imprimir(5)

# 2. Faça um programa para imprimir:

def imprimir2(n):
    for num in range(1,n+1):
        print([x for x in list(range(1, num+1))])
        
imprimir2(5)

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor 
# de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def validar(n):
    if n >= 0:
        print('P')
    else:
        print('N')

validar(-2)

# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o 
# custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def calc_imposto(custo, imposto_em_porcentagem):
    valor_final = custo * ((imposto_em_porcentagem + 100) / 100)
    return valor_final

print(calc_imposto(2000,10))
