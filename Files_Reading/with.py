"""
O with é um bloco de codigo que tem como objetivo trabalhar com um determinado objeto em um contexto,
onde tudo é finalizado após o bloco.

Muito utilizado junto ao open()
"""

with open('teste_open.txt') as arquivo:
    print(arquivo.read())
    arquivo.seek(0)
    print(arquivo.readlines())