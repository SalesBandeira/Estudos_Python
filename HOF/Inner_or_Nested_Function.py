# Inner ou Nested function são funções que possuem outras funções em seu bloco.

from random import choice
def saudacao(pessoa):
    def humor():
        return choice(['Olá ', 'Suma '])
    return humor() + pessoa

print(saudacao('Luana'))