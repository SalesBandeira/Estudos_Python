"""
Atributos são caracteristicas de um objeto.

Temos 3 tipos de atributos:

   - Atributos de instância.
        - São atributos declarados dentro dos metodos contrutores. Dentro dos metodos especiais.
   - Atributos de Classe .
   - Atributos Dinâmicos.
"""

# Atributos de instância.
# São atributos declarados dentro dos metodos contrutores. Dentro dos metodos especiais.

class Lampada:
    """Exemplo de Atributos de instancia, onde os atributos estão sendo 
        declarados dentro de um metodo construtor."""
    def __init__(self, voltagem, cor, ligada):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = ligada

# O primeiro parametro de qualquer metodo vai se referir a propria classe.
# por convenção damos o nome de self para esse parametro.
# self.nome = nome == o atributo nome do objeto lampada recebe nome

### Por default, no python, todos os atibutos são públicos. 
# Ou seja, os atributos podem ser acessados de qualquer parte do programa.  
# Caso seja de nossa vontade que esses atributos sejam tratados como privados, 
# utilizamos o __ antes do nome. Isso não torna o atributo inacessível
# o que ele faz é gerar um novo nome para dificultar o acesso a esse atributo
# O nome disso é Name Mangling.Fica nesse padrão:  _nomedaclasse__nomedoatributo

class Carro:
    """Exemplo de Atributos de instancia, onde os atributos estão sendo 
        declarados dentro de um metodo construtor. Nesse exemplo 
        tratamos de atributos privados."""
    def __init__(self, cor, marca, porte):
        self.__cor = cor
        self.__marca = marca
        self.__porte = porte


# Atributos de instacia são os atributo que fazem parte de todas as instacias da classe, pois foram definidos
# no metodo construtor. No momento da criação da instância apenas as declaramos. Os atributos dos objetos /
# instancia seram os mesmo, porém, os valores desses atributos serão diferentes para cada um.
