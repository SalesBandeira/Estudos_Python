"""
A herança multipla é um concenceito simples. Basicamente uma classe pode herdar os metodos e atributos
de mais de uma outra classe. Isso pode ocorrer de duas formas. 
    - Herança direta:
        a herança direta é quando na hora de criarmos a classe derivada delcaramos entre parênteses 
        todas as classes da qual ela deriva. Ou seja, estamos informando para o pytho, de forma expressa 
        que queremos que essa classe herde tudo das outras classes. 
        
        EX:
            class a:
                pass
            class b:
                pass
            class c(a,b):
                pass 

    - Herança indireta:
        A herança indireta é quando nossa classe recebe como parametro de derivação uma outra classe
        que já devira de uma terceira. 

        EX:
            class a:
                pass
            class b(a):
                pass
            class c(b):
                pass
"""

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        """Um construtor generico que pode ser utilizado como super para
            outras classes que partem de uma pessoa generica"""
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        """Função generica pertencente a uma classe mãe
            retorna o nome completo, valor inerente a toda sub classe
            que parta de uma pessoa."""
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda, produto):
        """
        Uma classe filha da classe pessoa que vair herdar do __init__
        de Pessoa os atributos nome, sobrenome e cpf."""
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
        self.__produto = produto

class ClienteCasa(Cliente):
    def __init__(self, nome, sobrenome, cpf, renda, produto, lote):
        super().__init__(nome,sobrenome,cpf,renda,produto)
        self.__lote = lote



cliente_casa1 = ClienteCasa('Lucas', 'Brando', 2148635148, 444523, 'casa', 402369)

print(cliente_casa1.nome_completo())
print(cliente_casa1.__dict__)