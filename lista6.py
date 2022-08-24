# programa para digitar 7 valores numericos para cadastrar em 1 unica lista e mostrar numeros pares e numeros impares.

valores = [[],[]]
for n in range(1, 8):
    num = int(input(f'Digite o {n}° valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f' Os números pares digitados foram {valores}')
valores[0].sort()
valores[1].sort()
print(f' Os números pares digitados foram {valores[0]}')
print(f' Os números impares digitados foram {valores[1]}')
