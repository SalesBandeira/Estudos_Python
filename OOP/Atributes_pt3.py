"""
Atributos dinâmicos.

São os atributos que são criados fora da classe, em tempo de execução.

para criarmos um atributo dinamico basta acessar um atributo que não exista e declararmos um valor para ele
ex:  objeto.atributo = valor do atributo
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
 
c1.tipo = 'Hatch' # Atributos dinâmicos
c2.tipo = 'Sedan'# Atributos dinâmicos

print(c1.id)
print(c2.id)
print(c1.valor)
print(c2.valor)
print(c1.tipo)
print(c2.tipo)

### Acessando os atributos de um objeto:

print(c1.__dict__)
print(c2.__dict__)

# Deletando atributos forma dinamica:

del c1.tipo

print(c1.__dict__)