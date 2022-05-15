"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
 uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e 
 passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este 
 valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a 
 execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja 
 informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, 
 exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. 
 O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor 
 da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""

def calc_jurosmulta(valor, dias_atraso):
    if dias_atraso > 0:
        valor  *= 1.03
        juros_multa = (valor * 0.01) * dias_atraso
        return valor+juros_multa
    else:
        return valor
     

def valorpagamento():
    qtde = 0
    total = 0
    while True:
        valor = int(input('Valor a ser pago: '))
        if valor == 0:
            break
        dias_atraso = int(input('Dias em atraso: '))
        qtde += 1
        total +=  calc_jurosmulta(valor, dias_atraso)
    print(f'Você realizou {qtde} pagamentos. O que resultou no total de R${total}')

valorpagamento()
