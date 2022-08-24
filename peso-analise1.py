# Leia o peso de 5 pessoas e mostre qual o menor e maior peso.

menor = 300
maior = 0
for c in range(0, 5):
   peso = float(input('Informe o peso: '))
   if peso < menor:
       menor = peso
   if peso > maior:
       maior = peso

print(f'O menor peso informado foi de {menor} e o maior peso de {maior}')
