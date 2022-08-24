#FOR
num = int(input('Digite um valor para saber o seu fatorial: '))
result = 1
print(f'Calculando {num}! = ', end='')
for c in range(num, 1, -1):
   result = result * c
   print(f'{c} x ', end='')

print(f'1 = {result}')

#While
num = int(input('Digite um valor para saber o seu fatorial: '))
result = 1
while num != 0:
   result = result * num
   num = num - 1
print(result)

#BIBLIOTECA
from math import factorial
num = int(input('Digite um valor para saber o seu fatorial: '))
print(factorial(num))

#WHILE_GUANABARA
num = int(input('Digite um valor para saber o seu fatorial: '))
c = num
result = 1
while c > 0:
   print(f'{c}', end='')
   print(f' x ' if c > 1 else ' = ', end='')
   result *= c
   c -= 1
print(result)