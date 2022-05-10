"""
Metodos é a forma como o objeto se comporta.
Nada mais sãoi doque funções dentro das classes.
Possuimos 3 tipos de metodos.

1 - o metodo construtor. 
    - Esse metodo é utilizado para definir o molde principal. Serve para construir a instância.
        Nessa função passamos os atributos principais dos objetos criados através da classe,
        alem do seu comportamento padrão.
        elas são definidas atraves do metodo mágico dunder init __init__

2 - Metodo de Instância.

São os metodos que são acessados e acionados a partir da instância.
Estão dentro do bloco da classe e o acionamos chamando a instância.metodo()
Esses metodos utilizam atributos da instancia para atuar.
Vamos utilizar metodos de instância sempre que, pasmem, precisarmos acessar os dados de uma instância.

3 - Metodos de Classe
    São os metodos que não estão ligado a nenhuma instância, e sim a prórpia classe.
    São declaradas a partir do decorator @classmethod
    recebem como parametro o (cls) uma convenção, abrevia class 
    São equivalentes aos metodos estáticos 
"""

#Metodo construtor
class Carro:
    imposto = 1.10 # atributo de classe
    contagem = 0
    @classmethod
    def contador(cls):
        print(f'Foram vendidos {cls.contagem} carros.')

    def __init__(self, cor, valor, marca):
        """Metodo construtor"""
        self.id = Carro.contagem +1
        self.cor = cor
        self.valor = (valor * Carro.imposto)
        self.marca = marca
        Carro.contagem = self.id
    
    def desconto(self, porcentagem):
        return self.valor * (100 - porcentagem) / 100
 

carro1 = Carro('Azul', 40000, 'Renault')
carro2 = Carro('Vermelho', 50000, 'Fiat')
carro3 = Carro('Prata', 100000, 'Toyota')
print(carro1.desconto(20)) # Metodo de instância sendo chamado

# Existe uma outra forma de chamarmos um metodo de instancia, acessando o self.

print(Carro.desconto(carro1, 20)) # repare que nessa caso, chamamos o self e declaramos a instancia como self

# de qualquer forma, chamamos a instância para usarmos esse metodo.

Carro.contador() # utilização  de um metodo de classe