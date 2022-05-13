"""
O python possui um modulo builtin para trabalharmos com datas, chama-se datetime.

O datetime, possui diversos metodos, classes, atributos e afins que podemos utilizar normalmente.
os principais são.

.time = trabalha com hora
.date  = trabalha com data
.datetime = trabalha com data e hora em conjunto

todos possuem o metodo .now que retorna a hora, data ou data e hora atual.

poswmoa utilizar qualquer uma dessa classes para trabalhar da forma que quisermos com datas, incluindo 
criar mpvas datas.

"""

import datetime

print(repr(datetime.datetime.now()))
print(datetime.datetime.now())

data = datetime.datetime.now()

print(data.replace(hour=18,minute=0,second=0,microsecond=0))

def date_conversor():
    """Retorna uma data inputada pelo user em formato datetime"""
    data = input('Informe sua data de nascimento: DD/MM/AA ')
    data = data.split('/')
    data = datetime.date(int(data[2]),int(data[1]),int(data[0]))
    return data


# acessando elementos do datetime

print(help(datetime))