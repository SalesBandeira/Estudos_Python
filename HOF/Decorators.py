"""
Decorators Functions ou funções decoradoras
São funções que trabalham em cima de outras funções as aperfeiçoando 

    - São funções
    - atuam em outras funções as aperfeiçoando
    - São exemplo de High Order Function
    - Utilizamos o @ como sintaxe, sintact Sugar
    - Para decorarmos ums função basta chamar o decorator acima da função a ser decorada com um @
    - Devemos pensar no decorar como embelezar, melhorar, aperfeiçoar. Não como em memorizar.

"""

def saudar(funtion): # a decorator sempre vai receber outra função como parametro
    def realy(): # inner
        print(f'Olá, seja muito bem-vindo')
        funtion() 
        print('Foi um prazer te conhecer') # no bloco devem estar as melhorias
    return realy # Retornamos a melhoria a ser aplicada, para isso usamos uma inner function

@saudar # Sintax Sugar: Estamos informando que o retorno da função saudar deve ser aplicada como decoradora
def nome(): # Abaixo da Sintax Sugar informamos a função que queremos decorar.
    print('Lucas')

nome() # Ao chamarmos a função, ela virá já decorada.