"""
Escreva um programa que imprima todos os números de Armstrong em base 10 que tenham até 6 dígitos.
"""

def armstrong(numero):
    for n in str(numero):
        print(int(n)**3)

armstrong(153)


"""


"""

def tabelaVerdade():
    x = 10
    y = 0
    for n in range(10):
        print(bool(x),end=" ")
        print(bool(y),end=" ")
        print(bool(x),end=" ")
        print(bool(y))

print(tabelaVerdade())
