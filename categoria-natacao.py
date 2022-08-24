# ler ano de nascimento 
# categoria na natação
# ate 9 anos mirim
# 14 infantil
# 19 junior
# 20 senior
# acima de 20 master

from datetime import date
nasc = int(input('Informe o ano de nascimento: \n'))
ano_atual = date.today().year
idade = ano_atual - nasc

print('Sua categoria na natação é: ')

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade == 20:
    print('Senior')
else:
    print('\033[4;37mMaster \033[m')