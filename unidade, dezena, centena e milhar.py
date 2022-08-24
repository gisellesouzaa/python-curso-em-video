# Ler um número de 0 a 9999
# mostre na tela cada um dos dígitos separados 

number = int(input('Digite um numero de 0 a 9999: '))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print('Analisando o número {}'.format(number))

print ('unidade: {}'.format(u))
print ('dezena: {}'.format(d))
print ('centena {}'.format(c))
print ('milhar: {}'.format(m))
