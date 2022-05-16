#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def count_num(num):
    return len(str(num))

print(count_num(44444))

# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.

def reverter(num):
    return print(str(num)[::-1])

reverter(123456789)

# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
# devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e 
# retorne NULL caso a data seja inválida.

import datetime
from time import strptime

from pyrsistent import m

def mes(data):
    data = strptime(data, '%d/%m/%Y')
    m = ''
    if data.tm_mon == 1:
        m = 'Janeiro'
    elif data.tm_mon == 2:
        m = 'Fevereiro'
    elif data.tm_mon == 3:
        m = 'Março'
    elif data.tm_mon == 4:
        m = 'Abril'
    elif data.tm_mon == 5:
        m = 'Maio'
    elif data.tm_mon == 6:
        m = 'Junho'
    elif data.tm_mon == 7:
        m = 'Julho'
    elif data.tm_mon == 8:
        m = 'Agosto'
    elif data.tm_mon == 9:
        m = 'Setembro'
    elif data.tm_mon == 10:
        m = 'outubro'
    elif data.tm_mon == 11:
        m = 'Novembro'
    elif data.tm_mon == 12:
        m = 'Dezembro'
    return print(f'{data.tm_mday} de {m} do ano de {data.tm_year}')

mes('03/02/2021')