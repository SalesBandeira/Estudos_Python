

from csv import writer

with open('teste.csv', 'w') as file:
    escritor = writer(file)
    filme = ''
    escritor.writerow(['Nome', 'Genero', 'Duração'])
    while filme != 'sair':
        if filme != 'sair':
            filme = input('Qual o filme?')
            genero = input('Qual o genero?')
            duracao = input('Qual a duração?')
            escritor.writerow()
        