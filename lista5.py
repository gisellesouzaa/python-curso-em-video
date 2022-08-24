# pedir valores numericos 
# add lista completa
# add lista impar
# lista par

# resolução 1:
lista = []
par = []
impar = []
while True:
    novo = (int(input('Digite um valor: ')))
    lista.append(novo)
    if novo % 2 == 0:
        par.append(novo)
    else:
        impar.append(novo)
    resp = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn': 
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')

# resolução 2 :
lista = []
par = []
impar = []
while True:
    novo = (int(input('Digite um valor: ')))
    lista.append(novo)
    resp = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn': 
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
