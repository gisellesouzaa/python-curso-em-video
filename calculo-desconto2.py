# calcule o valor do produto e a condição de pagamento
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

#Legenda de cores:
amarelo = '\033[1;30;43m'
cor_preco = '\033[4;45m'
fim = '\033[m'
roxo = '\033[1;30;43m'

price = float(input('{} Informe o valor do produto: R$ '.format(cor_preco)))
condition = int(input('''\n {2} Escolha uma condição de pagamento, sendo: 
{0} 1 {1} para à vista dinheiro/cheque;
{0} 2 {1} para à vista no cartão;
{0} 3 {1} para pagamento em até 2x no cartão; ou
{0} 4 {1} para 3x ou mais no cartão;

{3} Qual a forma de pagamento desejada? {2} '''.format(amarelo, fim, roxo, cor_preco)))

if condition == 1:
    print('Você terá 10% de desconto. O valor atual do produto é de R$ {:.2f}.'.format(price - price*10/100))
elif condition == 2:
    print('Você terá 5% de desconto. O valor atual do produto é de R$ {:.2f}.'.format(price - price*5/100))
elif condition == 3:
    print('O valor atual do produto é de R$ {:.2f}.'.format(price))
elif condition == 4:
    print('O produto terá acrescimo de 20% de juros. O valor atual é R$ {:.2f}. {}\n '.format(price + price*20/100, fim))
else:
    print('Condição de pagamento invalida.')
