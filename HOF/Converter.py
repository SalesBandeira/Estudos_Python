def conversor(*tipos):
    def decorador(function):
        def converte(*args, **kwargs):
            """
            Essa Função decoradora realiza a conversão dos tipos de dados pelo tipo de dados chamado na
            hora de utilizar o decorador.
            """
            new_args = []
            for valor, tipo in zip(args, tipos):
                new_args.append(tipo(valor))
            return function(*new_args, **kwargs)
        return converte
    return decorador

@conversor(float, float)
def dividir(a,b):
    return a/b

print(dividir(5,4))

