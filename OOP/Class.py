"""
Classes são o molde da OOP. É a partir das classes que definimos os atributos, e os metodos que
serão imbutidos em nossos objetos.

Classes são o modelo mapeado dos objetos da vida real representados de forma computacional.

Classes possuem:
    - Atributos: nada mais são do que as caracteristicas do nosso objeto. O que ele é? Como ele é?
        se o nosso obejto for um livro, teremos como caracteristicas: a cor, a quantidade de paginas, 
        o estilo literário e etc.,
    - Metodos: São as ações do objeto, o que ele faz? como faz e como deve fazer. Metodos são funções.
        São os comportamentos do objeto.

A instancias mapeadas do mundo real recebem o nome de entidade.  


Criamos uma classe utilizando a palavra reservada class. Seguido do nome da classe e doi pontos.

Quando criamos uma classe estamos criando um DataType. 
Por convenção, a classes são CamelCase, palavras juntas sempre iniciadas com letra maiúscula.
"""

class Nome:
    pass

class Idade:
    pass

class Altura:
    pass

name = Nome()
heigh = Altura()
age = Idade()


print(type(heigh)) # dataType Altura
print(type(age)) # DataType Idade
print(type(name)) # DataType Nome