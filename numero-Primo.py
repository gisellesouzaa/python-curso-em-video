# leia um número inteiro e verifique se é numero primo 

n = int(input('Informe um número: '))
contador = 0
outro = 0

for c in range(1, n+1):
   if n % c == 0:
       contador += 1
       print(c, end='- ')
   else:
       print(c, end='- ')
       outro += 1

if contador == 2:
   print (f'O número informado foi divisivel {contador} vezes e por isso ele é primo')
else:
   print(f'O número informado foi divisivel {outro} vezes e por isso ele NÃO é primo')
