
"""
Para trabalharmos com CSV podemos utilizar a biblioteca csv, para isso basta importa-lá.

Para leitura, podemos utilizar duas funções desse pacote.

    A função reader():
        essa função gera um iteravel em forma de lista com cada linha do arquivo csv.
        podemos atuar em cima dela com o for e utilizarmos o slice '[]' para acessarmos o valor 
        de cada celula na linha. Essa função retorna também o cabeçario.

    A função DIctReader():
        Também retorna um iteravel que pode ser trabalhado com o for.
        porem essa função ordena o arquivo no formato de um dict ordenado,
        onde a chave sempre vai ser o nome do cabeçario.

    
        

"""

# metodo padrão de leitura, não recomendado quando tratamos CSV.
with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    print(dados)


# metodo utilizando a função reader do pacote csv
from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'O(a) lutador(a) {linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}')

#metodo utilziando a função DictReader do pacote csv

from csv import DictReader

with open('lutadores.csv') as arquivo:
    dict_reader = DictReader(arquivo)
    print(type(dict_reader))
    for linha in dict_reader:
        print(f"O(a) lutador(a) {linha['Nome']}  nasceu em {linha['País']} e mede {linha['Altura (em cm)']} ")
