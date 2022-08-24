# ler duas notas
# calcular media 
# <5  reprovado
# 5 e 6.9 recuperação
# => 7 aprovado

print('Calculando a média escolar:')
n1 = float(input('Insira a primeira nota para calcular a média: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2)/2 

if media < 5:
    print('Infelizmente você foi \033[1;31m REPROVADO \033[m.')
elif media < 7:
    print('Você está em \033[7;33m RECUPERAÇÃO \033[m')
else:
    print('Sua media foi {2} e você está {0} APROVADO! Parabéns! {1}'.format('\033[1;97;42m','\033[m', media))
