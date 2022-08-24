n = soma = c = 0
n = int(input('Digite o numero [999 para parar]: '))
while n != 999:
   soma += n
   c += 1
   n = int(input('Digite o numero [999 para parar]: '))
print(f'Você digitou {c} termos e a soma é {soma}')
