import json

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Funcionario(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.__matricula = matricula
    
    @property
    def matricula(self):
        return self.__matricula


func1 = Funcionario('Ricardo', 223647)

print(func1.nome)
print(func1.matricula)
print(func1.__dict__)
ret = json.dumps(func1.__dict__)
print(ret)
