# ler 3 numeros e dizer qual é o menor e maior

a = float(input('Insira o primeiro número: '))
b = float(input('Insira o segundo número: '))
c = float(input('Insira o terceiro número: '))

print('¨-¨' * 10)

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {:.0f}.'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('E o maior número é {:.0f}!'.format(maior))

print('¨-¨' * 10)
