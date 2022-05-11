"""
Por convençaõ, no python, foi decidido que devemos utilizar nossos atributos sempre de forma 
privada (__atributo). Isso definido, somente devemos acessar um atributo dentro de sua classe.
Porém, como já estudado, caso queiramos acessar um atributo privado basta sabermos do nam Mugglin
_NomeClasse__nomeatributo. Por mas que seja possível esse acesso, ele não é a forma correta.
Para isso o ideal seria criarmos ou metodos getters e setters que nada mais são do que funções 
cujo o unico objetivo é retornar um alterar um atributo. Não tem nada de errad em utilizarmos esse modelo
porém, isso é muito herança do java, a forma mais inerente ao python para isso seria a criação de properties
Propriedades da classe. 

uma propriedade é um metodo com um decorator. Esse decoretor se chama property.

    Ex:
        @property
        def produto(self):
            return self.__produto

    A propriedade acima dá acesso ao atributo privado __renda
    para o chamarmos é bem parecido com ummetodo, a diferença é que não colocamos os parenteses após 
    o nome da propriedade.

Podemos tbm definir propriedade setters.
Para isso, basta decorarmos o nosso metodo setter com o nome do nosso atributo anteriormente criado

    @produto.setter
    def produto(self, novo_produto):
        self.__produto = novo_produto

para utilizarmos é como se estivessimos atibuindo um novo valor a uma variável.

cliente1.produto = novo_produto do objeto cliente1, no seu atributo produto, quero incluir o novo produto

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

    @property
    def renda(self):
        return self.__renda
    
    @property
    def produto(self):
        return self.__produto
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @produto.setter
    def produto(self, novo_produto):
        self.__produto = novo_produto



cliente1 = Cliente('Roberto', 'Souza', 62358692563, 4500, 'Casa')

print(cliente1.renda) # utilização da propriedade getter
print(cliente1.produto) # utilização da propriedade getter
cliente1.produto = 'carro' # utilização da propriedade setter
print(cliente1.produto) # utilização da propriedade getter