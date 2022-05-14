"""
Alguns dos metodos mais utilizados com datetime

"""

#.weekday retorna o dia da semana em numeros de 0 a 6, sendo o 0 a segunda.

import datetime

def nascimento(data):
    data = data.split('/')
    nasc = datetime.datetime(int(data[2]),int(data[1]),int(data[0]))
    return nasc

def dia_nascimento():
    """Retorna o dia da semana de um aniversário"""
    data = input('Qual o seu aniversário? ')
    dia_aniv = nascimento(data)
    if dia_aniv.weekday() == 0:
        return print('Você nasceu em uma segunda')
    elif dia_aniv.weekday() == 1: 
        return print('Você nasceu em uma terça')
    elif dia_aniv.weekday() == 2: 
        return print('Você nasceu em uma Quarta')
    elif dia_aniv.weekday() == 3: 
        return print('Você nasceu em uma Quinta')
    elif dia_aniv.weekday() == 4: 
        return print('Você nasceu em uma Sexta')
    elif dia_aniv.weekday() == 5: 
        return print('Você nasceu em uma Sábado')
    elif dia_aniv.weekday() == 6: 
        return print('Você nasceu em uma Domingo')

# dia_nascimento()

# Formatando datas

agora = datetime.datetime.now()
print(agora)
convertido = agora.strftime('%d/%m/%Y')
print(convertido)

# transformando string em datetime, modo 2. strinptime()
# a função strinptime formata uma string para o formato datetime.
# essa função recebe dois parametros. o priomeiro é a string a ser formatada e a segunda é o formato em 
# que a string se encontra
#   EX:

data = '20/03/1998'
print(data)
conv_data = datetime.datetime.strptime(data, '%d/%m/%Y')
print(conv_data)

# refatorando a função nascimento
def nascimento1(data):
    nasc = datetime.datetime.strptime(data, '%d/%m/%Y')
    return nasc

def dia_nascimento1():
    """Retorna o dia da semana de um aniversário"""
    data = input('Qual o seu aniversário? ')
    dia_aniv = nascimento1(data)
    if dia_aniv.weekday() == 0:
        return print('Você nasceu em uma segunda')
    elif dia_aniv.weekday() == 1: 
        return print('Você nasceu em uma terça')
    elif dia_aniv.weekday() == 2: 
        return print('Você nasceu em uma Quarta')
    elif dia_aniv.weekday() == 3: 
        return print('Você nasceu em uma Quinta')
    elif dia_aniv.weekday() == 4: 
        return print('Você nasceu em uma Sexta')
    elif dia_aniv.weekday() == 5: 
        return print('Você nasceu em uma Sábado')
    elif dia_aniv.weekday() == 6: 
        return print('Você nasceu em uma Domingo')

#dia_nascimento1()