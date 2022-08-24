from math import trunc
num = float(input('Digite um valor com casas decimais: '))
print('O numero digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

#Alternativa1: 
# import math
# num = float(input('Digite um valor com casas decimais: '))
# print('O numero digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

# Alternativa2:
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))

