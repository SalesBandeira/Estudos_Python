"""
Abstração e encapsulamento:

O paradgma da orientação a objeto possui 2 pontos teoricos de bastante destaque. 

o primeiro, de abstração, diz respeito ao fato de que temos que abstrair, retirar, do usuário
informações que ele não precisa saber para utilizar o software. Apenas devemos deixa que ele veja
as informações fundamentais para que possa utiliza-lo.

o encapsulamento trata da forma como a clase coloaca em uma capsula os seus metodos e funções.
os deixa em um ambiente controlado onde podem ser replicados sem maiores complicações
para suas respectivas instancias.

"""

class Cc:

    codigo = 399
    agenc = 4995

    def __init__(self, saldo, limite):
        self.conta = Cc.codigo +1
        self.agencia = Cc.agenc +1
        self.saldo = saldo
        self.limite = limite
        Cc.codigo = self.conta
        Cc.agenc = self.agencia
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')
        
    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
        else:
            print('Talvez você queira sacar um valor? \nQue tal tentar essa função?')
    
    def pagar_credito(self, valor):
        if self.limite >= valor:
            self.limite -= valor
        else:
            print('Limite insuficiente')
    
    def pagar_debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Sem saldo suficiente')


conta1 = Cc(1000, 2000)
conta2 = Cc(2000, 5000)

print(conta1.saldo)
conta1.sacar(800)
conta1.sacar(400)
print(conta1.limite)
conta1.pagar_credito(1500)
print(conta1.limite)