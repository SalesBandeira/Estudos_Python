"""
A função seek() funcioana de forma em que podemos manipular o cursor na função open().
Vai receber um atributo que nada mais é do que o indice no qua o cursor deve ser iniciado

open sempre, no momento da leitura (.read()) retorna uma string, portando cada caractere dessa string 
possui uma posição com indice. 

"""

def read(file):
    with open(file) as arquivo:
        print(arquivo.read())
        arquivo.seek(0)
        print(arquivo.read())
        arquivo.seek(0)

read('teste_open.txt')