"""
Após termos o nosso objeto mapeado pela classe, tendo todas as suas características declaradas no metodo de 
construção, conseguiremos então ciar objetos a partir de um processo chamado de instanciação.

Ora, um objeto nada mais é do que uma instância da classe. ou seja, algo que surge a partir do molde da classe.

Ao criarmos uma instância, devemos informar todos os atributos declarados como parametro no construtor.

Podemos pensar em objetos como variáveis do tipo de dado definido na classe.
Objetos podem fazer parte de outros objetos, tendo esse segundo acesso a todos os atributos e metodos 
do primeiro.
"""

class Lampada:
    def __init__(self, cor, voltagem, tipo):
        self.cor = cor
        self.voltagem = voltagem
        self.ligada = False
        self.tipo = tipo
    
    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def mostra_tipo(self):
        print(f'O tipo dessa lampada é {self.tipo}')


class Tipo:
    def __init__(self, t, p):
        self.t = t
        self.p = p


lamp1 = Lampada('azul', 220, ['Fluorecente', 'barata']) # fase de instanciação. Ou seja, a criação do objeto.

print(lamp1.ligada) # acessando o valor de um atributo da instância
lamp1.ligar_desligar() # utilizando um metodo na instância para alterar seu comportamento.
print(lamp1.ligada) # acessando o valor de um atributo da instância

tipo1 = Tipo("LED", "Cara")

lamp2 = Lampada('branca', 110, tipo1) # usando outra objeto como atributo

lamp1.mostra_tipo()
lamp2.mostra_tipo()

