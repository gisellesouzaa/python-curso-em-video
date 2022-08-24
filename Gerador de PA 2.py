print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
quant_termo = 5
c = 0
while c < quant_termo:
   print(f'{termo} - ', end='')
   termo += razao
   c += 1
print('PAUSA')
quant_termo2 = int(input('Quantos termos você quer mostrar a mais? '))
novo_termo = quant_termo + quant_termo2

while c < novo_termo:
   print(f'{termo} - ', end='')
   termo += razao
   c += 1
