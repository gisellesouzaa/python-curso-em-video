# pedir valores numericos 
# quant elementos
# ordem decrescente de inserção 
# se o 5 esta na lista


lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    if resp in 'Nn': 
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else: 
    print('O valor 5 não está na lista')
