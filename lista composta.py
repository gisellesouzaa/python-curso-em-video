galera = list()
dado = list()
maior_peso = menor_peso = 0
resp = ' '
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior_peso = menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
    galera.append(dado[:])
    dado.clear()
    resp = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if resp in 'Nn':
        break
print(f'Os dados foram {galera}')
print(f'Foi cadastrado {len(galera)} pessoas na lista.')
print(f'O maior peso foi de {maior_peso} quilos. Peso de ', end='')
for p in galera:
    if p[1] == maior_peso:
        print(f'{p[0]}', end=', ')
print(f'\nO menor peso foi de {menor_peso} quilos. Peso de ', end='')
for p in galera:
    if p[1] == menor_peso:
        print(f'{p[0]}', end=', ')
