# Ler nome, idade e sexo de 4 pessoas. mostrar media de idade do grupo , nome do homem mais velho,  e quantas mulheres tem menos de 20 anos.

velho = 0
soma = 0
nome_velho = ' '
quant_mulheres = 0
tem_homens = False
tem_mulheres = False
for c in range(1,5):
   print(f'---- {c}ª PESSOA ----')
   n = str(input('Nome: '))
   i = int(input('Idade: '))
   s = str(input('Sexo [M/F]: ')).upper()
   soma += i
   if s == 'M':
       tem_homens = True
       if velho < i:
           velho = i
           nome_velho = n

   if s == 'F':
       tem_mulheres = True
       if i < 20:
           quant_mulheres += 1
if tem_homens == True:
   print(f' O {nome_velho} tem {velho} anos e é o homem mais velho')
if tem_mulheres == True:
   print(f'No grupo tem {quant_mulheres} mulheres menores de 20 anos.')

print(f'A media das idades é {soma/4}')