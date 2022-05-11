"""
Herança.

A herança é um conceito que utilizamos para reduzir a quantidade de código reaproveitando outros códigos já
criados. A partir da gerança, podemos acessar, atributos e metodos de outras classes.

Para utilizarmos a herança de forma correta devemos lembrar do conceito de encapsulamento.  Ou seja, devmos
sempre procurar um molde generico como classe onde, a partir dele serão criados as instâncias.

As vezes vamos ter moldes bem parecidos mas que possuem uma diferecia substancial.
A ideia gira em torno de que, por mais que essas classes possuam diferenças em seu core, elas também possuem
diversas semelhanças. Ai é onde a herança entra. 

Criamos uma classe mãe, que vai possuir os atributos e metodos que todos os agora classes filhas possuem
em comum, encapsulando essa selhança. A part, declaramos para o Python que essa classe é um subproduto
da classe anterior atraves da delcaração da classe mãe entre parenteses apos a criação da classe
filha. 

    EX: 
        class mae:
            pass

        class filha(mae):
            pass

Tudo que a classe mãe possuir de atributo e metodo será herdado para a filha.  Porém, para isso, 
precisamos tbm informar os atributos tanto no contrutor da classe filha como na hora da utilização
de um novo metodo chamado super(). Esse metodo virá logo após o init. chamamos o metodo e declaramos os 
atributos escolhidos. AS classes mãe tbm são conhecidas como classe super, clase base, classe generica.
chamar o nome da classe mãe entre parenteces é informar ao python a correlação entre essas duas classes.
no metodo contrutor da classe filha vou delcarar normalmente os atributos que as instancias devem possuir.
no metodo super() estou falando ao python  que os valores dos atributos informados no construtor da filha
serão herdados da classe mãe. 

    Ex:
        class mae:
            def __init__(self, cor, preco)

        class filha(mae):
            def __init__(self, cor,preco,marca)    
            super().__init__(cor, preco)
            self.marca = marca

os metodos também serão herdados normalmente. Porém, caso seja do interesse do desenvolvedor existe uma 
aplicação na herança chamada de Overriding, que nada mais é do que passar uma nova instrução para um metodo
da classe mãe dentro da classe filha. basta reescrever o metodo com o mesmo nome e as novas instruções.
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        """Um construtor generico que pode ser utilizado como super para
            outras classes que partem de uma pessoa generica"""
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def nome_completo(self):
        """Função generica pertencente a uma classe mãe
            retorna o nome completo, valor inerente a toda sub classe
            que parta de uma pessoa."""
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda, produto):
        """
        Uma classe filha da classe pessoa que vair herdar do __init__
        de Pessoa os atributos nome, sobrenome e cpf."""
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda
        self.produto = produto

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula, setor):
        """Uma classe filha da classe pessoa que vair herdar do __init__
        de Pessoa os atributos nome, sobrenome e cpf. """
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula
        self.setor = setor

cliente1 = Cliente('Roberto', 'Souza', 62358692563, 4500, 'Casa')
funcionario1 = Funcionario('Luana', 'Silva', 59536412385, 256987, 'Imobiliário')

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

