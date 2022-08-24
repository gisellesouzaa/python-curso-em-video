matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = scol = maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-'*30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        #soma valores pares:
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print( )
print('=-'*30)

print(f'A soma dos valores pares é {spar}')
# soma dos valores da 3a coluna
for l in range (0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {scol}')

#maior valor da segunda linha
for c in range (0,3):
    if matriz[1][c] > maior:
        maior = matriz[1 ][c]
print(f'O maior valor da segunda linha é {maior}')
