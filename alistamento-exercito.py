# ler ano de nascimento e informar:
# Se ele ainda vai se alistar. Quanto tempo falta
# Se está na hora de se alistar. “se alista agora”
# Se já passou o tempo do alistamento quanto tempo passou

from datetime import date

print('Verificando prazo para o alistamento militar')
year = int(input('Informe o ano do seu nascimento: '))
yeartoday = date.today().year
idade = yeartoday - year

if idade <= 17:
    print('Falta {} anos para você ficar apto ao alistamento.'.format(18 - idade))

elif idade == 18: 
    print(' Você está na idade do alistamento. Se aliste agora!.')

else: 
    print('Já passou o prazo do seu alistamento. Você está atrasado {} anos. Regularize sua situação!'.format(idade - 18))
