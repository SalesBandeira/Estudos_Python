"""
O metodo Super é um metoo que chama a classe mãe/super se ela tiver sido declarada na classe em questão.
metodo:
    super().o_que_queremos_acessar_da_classe_mãe

Vale ressaltar que podemos chamar o super para acessar QUALQUER atributo OU metodo da classe super.

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
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda, produto):
        """
        Uma classe filha da classe pessoa que vair herdar do __init__
        de Pessoa os atributos nome, sobrenome e cpf."""
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
        self.__produto = produto

cliente1 = Cliente('Lucas', 'Brando', 2148635148, 444523, 'casa')

