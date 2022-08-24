resp = 'S'
n = c = media = soma = maior = menor = 0
while resp in 'Ss':
   n = int(input('Digite um numero: '))
   c += 1
   soma += n
   if c == 1:
       maior = menor = n
   else:
       if n > maior:
           maior = n
       if n < menor:
           menor = n
   resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]

print(f'Você digitou {c} numeros e a media foi {soma/c}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
