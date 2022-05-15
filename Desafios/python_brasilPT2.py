"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o
 programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo 
 menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. 
 como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um 
 parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário 
 repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""

def conv_horas(hora):
    hora = hora.split(':')
    hora_convertida = int(hora[0])
    if hora_convertida > 12:
        hora_convertida -= 12
        return print(f'{hora_convertida}:{hora[1]} PM')
    return print(f'{hora_convertida}:{hora[1]} AM')

# hora = input('Digite um horário: ')
# conv_horas(hora)

def conv_horas2(hora,minutos):
    """ Converte um horario em formato 
        24H para o formato 12H"""
    if hora > 12:
        hora -= 12
        return f'{hora}:{minutos} P.M'
    return f'{hora}:{minutos} A.M'

def conver():
    """Realiza um loop para converter os horarios 
        em formato 24H para formato 12H"""
    continuar = ''
    while continuar != 'não':
        hora = int(input('Digita um numero para a hora: '))
        minutos = int(input('Digita um numero para os minutos: '))
        print(conv_horas2(hora, minutos))
        continuar = input('Deseja continuar? ')

conver()



