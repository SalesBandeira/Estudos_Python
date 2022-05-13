"""
Podemos realizar calculos com datas normalmente em python.  Basta que as datas sejam Dtype datetime.

operações de subtração entre dtype datetime geram um novo tipo dtype chamado datetime.timedelta

"""
import datetime
agora = datetime.datetime.now()
evento = datetime.datetime(2022,10,1)
delta = evento - agora

print(type(delta))
print(delta)
print(f'faltam {delta.days} dias para a migração')

def vencimento_boleto(data_compra):
    """Retorna a data de vencimento do boleto da compra."""
    regra_boleto = datetime.timedelta(days=3)
    data_compra += regra_boleto
    return data_compra

compra = datetime.datetime.now()

print(vencimento_boleto(compra))