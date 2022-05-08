"""
High Order Functions

Funções de maior grandeza são funções que requerem um grau mais elevado de complexidade
pois podempossuir outra função dentro delas, podem possuir funções externas como argumentos, lambdas
generators e afins.

"""

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def calcular(function,a,b):
    ### Retorna um valor a ser calculado 
    ## de acordo com a função escolhida
    return function(a,b)

print(calcular(multiplicar,5,5))
print(calcular(somar,5,5))
print(calcular(subtrair,5,5))