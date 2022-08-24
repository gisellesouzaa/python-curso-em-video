ficha = list()
while True:
    nome = str(input('Digite um nome: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2
    ficha.append([nome, [n1, n2], media])
    cont = input('Quer continuar [S/N]: ').upper().strip()[0]
    if cont == 'N':
        break
print(ficha)
