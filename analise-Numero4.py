# Ler 6 números inteiros e somar apenas os números pares

s = 0
cont = 0
for c in range (1, 7):
   n = int(input('Digite um número: '))
   if n % 2 == 0:
       s += n
       cont = cont + 1
print(f' Você digitou {cont} números pares e a soma deles é {s}.')

