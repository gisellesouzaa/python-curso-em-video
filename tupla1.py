tupla = (int(input('Digite um numero: ')), 
int(input('Digite outro numero: ')), 
int(input('Digite mais um numero: ')), 
int(input('Digite o último numero: ')))
print('Você digitou os valores: ', tupla)

print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O valor 3 apareceu na {}ª posição'.format(tupla.index(3)+1))
else: 
    print('O valor 3 não foi digitado em nenhuma posição')
cont = 0
for n in tupla:
    if n % 2 == 0:
        cont += 1 
print('Foram digitados {} numeros pares'.format(cont))
