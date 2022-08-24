print('         BANCO CEV          ')
print('-' * 40)
ced = 50
quant_ced = 0
sacar = int(input('Que valor você quer sacar? R$ '))
resto = sacar
while True:
   while resto >= ced:
       resto -= ced
       quant_ced += 1
   if quant_ced != 0:
       print(f'Total de {quant_ced} cedulas de R$ {ced:.2f}')
   elif ced == 50:
       ced = 20
   elif ced == 20:
       ced = 10
   elif ced == 10:
       ced = 1
   quant_ced = 0
   if resto == 0:
       break
