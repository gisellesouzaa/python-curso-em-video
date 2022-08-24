print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
quant_termos = int(input('Quantos termos você quer mostrar? '))
print('~' * 20)
c = 3
t1 = 0
t2 = 1
t3 = t1 + t2
c = 0
print(f'{t1} - {t2} - ', end=(''))
while c < quant_termos:
   print(f'{t3} - ', end='')
   t1 = t2
   t2 = t3
   t3 = t1 + t2
   c += 1
print(f'Finalizada com {c} termos')