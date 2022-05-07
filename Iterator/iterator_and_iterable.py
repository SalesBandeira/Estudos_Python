"""
O que é um iterator e o que é um iterable?

um iterable é um objeto que pode ser quebrado em mais de uma parte.
uma string de dois caracteres ou mais, uma lista, uma tupla, um set e etc.,

Já um iterator nada mais é do que o objeto capaz de quebrar um iterable e passar por cada uma das partes.
absorvendo o seu valor, um por vez. 

Um loop nada mais é do que uma função que pega um iterable e extrai um iterator.

Um loop pega o iterable e aplica a função iter(), essa função é a responsável por quebrar o iterable.
então, o loop vai aplicar a função next() enquanto os parametros da função forem atendidos. 
O next() é a função que passa por cada uma das partes do já quebrado iterable.
"""

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

my_for(list(range(0,10)))


