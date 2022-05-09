"""
Ao utilizarmos decoradores passamos por um probelama comum onde os metadados da função decorada são perdidos 
após a decoração. Nolugara deles, são colocados os metadados da função decoradora.


"""
def saudar(funtion):
    def realy(*args, **Kwargs):
        """ Essa função sauda todos"""
        print(f'Olá, seja muito bem-vindo')
        funtion(*args, **Kwargs) 
        print('Foi um prazer te conhecer')
    return realy

@saudar
def nome(name):
    """Essa função requer um nome"""
    print(name)

print(nome.__name__) # o nome que vai vir é o da função decoradora
print(nome.__doc__) # a doc que vai vir é o da função decoradora


# para resolvermos esse problema precisamos utilizar o wraps, função que existe dentor de functools.

from functools import wraps
def saudar1(function):
    @wraps(function)
    def realy1(*args, **Kwargs):
        """ Essa função sauda todos"""
        print(f'Olá, seja muito bem-vindo')
        function(*args, **Kwargs) 
        print('Foi um prazer te conhecer')
    return realy1

@saudar1
def nome1(name):
    """Essa função requer um nome"""
    print(name)

print(nome1.__name__) # o nome que vai vir é o da função decorada
print(nome1.__doc__) # a doc que vai vir é o da função decorada

# O wraps nada mais é do que uma função decoradora ela mesma. Sua função é preservar os metadados
# da função que for decorar. Ao chamarmos ela debtri da função decoradora logo após a definição da função
# informamos ao python que queremos preservars os metadados dela.