lista = list()
while True:
    novo = (int(input('Digite um valor: ')))
    if novo not in lista:
        lista.append(novo)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não foi add a lista')
    continua = str(input(r'Você quer continuar [s/n]: ')).upper().strip()[0]
    if continua == 'N':
        break
print('-=' * 30)
lista.sort() 
print(f'Você digitou os valores: {lista}')
