# Ler a ano de nascimento de 7 pessoas. E conte quantos são maiores e menores de idade.

menor = 0
maior = 0
from datetime import date
for c in range(1, 8):
   ano_nasc = int(input('Informe o ano de nascimento: '))
   ano_atual = date.today().year
   if ano_nasc < ano_atual-18 :
       menor += 1
   else:
       maior += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores de idade.')
