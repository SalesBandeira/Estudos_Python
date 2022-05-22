"""
Crie um programa que recebe uma lista de inteiros e um valor que 
deve ser buscado. O programa deve retornar o índice onde o valor foi encontrado,
 ou -1, caso não encontre o valor.
"""

import enum


def serch_array(valor_procurado,array):
    """Retorna o indice de um valor em uma lista. Caso não encontre, retorna -1"""
    for i, v in enumerate(array):
        if v == valor_procurado:
            return print(f'O indice do valor praocurado é {i}')
    return print('-1')


serch_array(12,[1,4,6,8,2,5,9,12,3,11])

"""
Escreva um programa que cria uma lista de 100 números aleatórios inteiros ordenados 
e solicita um número para o usuário. Use a busca binária para encontrar a posição do número 
fornecido na lista, ou retorne -1 se ele não for encontrado.
"""

def bin_search(valor_procurado,array):
    for i, v in enumerate(array[33:65]):
        if valor_procurado == v:
            print(f'o indice é: {i}')
    if valor_procurado > v:
        for i, v in enumerate(array[66:]):
            if valor_procurado == v:
                print(f'o indice é: {i}')
    else:
        for i, v in enumerate(array[:32]):
            if valor_procurado == v:
                print(f'o indice é: {i}')
    

bin_search(99,range(1,100))


"""
Algoritmo que Verifica se um Texto é um Palíndromo

"""

def Palindromo_val(pol):
    val = pol[::-1]
    if pol == val:
        return print('A palavra é um palíndromo')
    return print('A palavra não é um palíndromo')

Palindromo_val('ana')
Palindromo_val('anali')
Palindromo_val('arara')