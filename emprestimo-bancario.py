# pedir valor da casa, salário, prazo que quer comprar em anos
# calcule o valor da prestação
# se prestação for menor que 30% da renda, mostrar simulação
# se for maior que 30%, empréstimo negado

print('\033[4;31m Financiamento de imóvel!\033[m')
print('Para simular o financiamento do imóvel informe =>')
name = str(input('Nome: '))
home = float(input('Valor do imóvel: R$'))
cash = float(input('Valor do salário comprador: R$'))
year = int(input('Prazo do financiamento (de 1 a 35 anos):'))

prazo = year*12
prestacao = home / prazo
comprometimento = cash * 30/100

print ('...' * 25)
print ('Analizando...')
print ('...' * 25)
from time import sleep
sleep (3)

if prestacao <= comprometimento:
    print('{3} Parabéns {4}! \n O seu financiamento foi aprovado com parcelas de R$ {0:.2f} em {1} meses!{2}'.format(prestacao, prazo, '\033[m', '\033[1;32m', name))
else:
    print('{1}Infelizmente o credito foi reprovado! {0}'.format('\033[m', '\033[1;31m'))
