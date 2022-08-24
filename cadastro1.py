continua = 'S'
maior18 = 0
quant_homem = 0
menor20 = 0
while continua in 'Ss':
   print('Cadastre uma pessoa')
   print('-' * 20)
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
   print('-' * 20)
   if idade > 18:
       maior18 += 1
   if sexo == 'M':
       quant_homem += 1
   if sexo == 'F' and idade < 20:
       menor20 += 1
   continua = str(input('Quer continuar [S/N]: '))
   print('-' * 20)
print(f'''Total de pessoas com mais de 18 anos: {maior18}
Total de homens cadastrados: {quant_homem}
Total de mulheres com menos de 20 anos: {menor20}''')
