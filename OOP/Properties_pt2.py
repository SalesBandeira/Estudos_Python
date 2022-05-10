"""
Atributos de classe:

Ao contrario dos atributos de instancia onde declaramos o seu valor no momento da criação da instância, 
Criamos atriibutos de classe quando declaramos esse valor diretamente na classe. Fazendo com que
todos as instâncias dessa classe possuem o mesmo atributo com o mesmo valor.

"""


class Carro:
    imposto = 1.10 # atributo de classe
    contagem = 0
    def __init__(self, cor, valor, marca):
        self.id = Carro.contagem +1
        self.cor = cor
        self.valor = (valor * Carro.imposto)
        self.marca = marca
        Carro.contagem = self.id

c1 = Carro('vermelho', 40000, 'Gol')
c2 = Carro('azul', 50000, 'Renault')

print(c1.id)
print(c2.id)
print(c1.valor)
print(c2.valor)

# Utilizamos atributos de classe para estabelecermos pontos fixos em nossa classe.
# pontos que sabemos que são de igual valor para qualquer instância que venha a ser criada
# a partir desse molde.
