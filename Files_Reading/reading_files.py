class File:
    def write_file(file):
        with open(file,'a+') as arquivo:
            arquivo.write('\n teste3')
    
    
    def read_file(self, file):
        with open(file,'r') as arquivo:
            print(arquivo.read())

meu_arquivo = File()
meu_arquivo.read_file('teste_open.txt')