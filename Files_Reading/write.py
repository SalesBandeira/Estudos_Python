"""
Para abrirmos em modo de escrita padrão, a chave é 'w'
sempre que abrimos com essa chave, um novo arquivo vai ser criado dozero. Se ouverem informações no antigo
essas informações serão perdidas e sobre escritas pelas novas. 

"""

with open('novo_teste.txt', 'w') as arquivo:
    arquivo.write('Teste na escrita de aquivos com python\n')
    arquivo.write('novo teste\n')
    arquivo.write('teste final.')