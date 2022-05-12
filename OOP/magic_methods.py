"""

TOda classe herda primeiramente de object.
Os metodos magico nada mais são doque os metodos inbutidos em object.
A maior parte das funções que ja conhecemos builtin do python (len, max, reduce, min etc.,) naturalmente
não vão conseguir interagir com os objetos instanciados. Para isso precisamos reimplementar esses metodos
atraves dos metodos magicos. Os metodos Dunder.

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
    
    def __len__(self):
        """Retorna o len de CPF"""
        contagem = []
        for n in str(self.__cpf):
            contagem += n
        return len(contagem)
    
    def __str__(self) -> str: # Faz com que a classe em sí retorne o parametro como string
        return self.__nome   
    


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



cliente_casa1 = ClienteCasa('Lucas', 'Brando', 21486351482, 444523, 'casa', 402369)

print(cliente_casa1)
print(len(cliente_casa1)) 