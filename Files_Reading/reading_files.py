"""
A função open() é utilizada para acessar arquivos.

a função aceita dois parametros, a primeira é o nome ou path para o arquivo. 
A segunda é o que iremos fazer com o arquivo segundo o sequinte modelo, sempre entre aspas:

'r' abre par leitura somente, se nada for informado, essa opção é default.
'w'	abre para leitura, apaga todos os dados antes.
'x'	ccria um novo arquivo e o abre para leitura,
'a'	abre para leitura, adcionando ao final da ultima linha
'b'	binary mode
't'	text mode (default)
'+'	abre para atualizar, leitura e escrita
'U'	universal newline mode (deprecated)

"""

# Chamamos os atributos .read ou .write par usarmos o arquivo de fato.

class File:
    def write_file(file):
        with open(file,'a+') as arquivo:
            arquivo.write('\n teste3')
    
    
    def read_file(self, file):
        with open(file,'r') as arquivo:
            print(arquivo.read())

meu_arquivo = File()
meu_arquivo.read_file('teste_open.txt')