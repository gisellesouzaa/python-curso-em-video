# < 18.5 Abaixo do peso
# entre 18.5 e 25 peso ideal
# 25 até 30 sobrepeso
# 30 até 40 obesidade
# acima dos 40 obesidade mórbida

print('-_-' * 8)
print('\033[7m CALCULANDO O IMC \033[m')
print('-_-' * 8)

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

print( '...' * 8)
print ('O seu IMC atual é {:.1f}!'.format(imc), end=' ')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está com obesidade. Cuide-se!')
else:
    print('Você está com obesidade mórbida.')