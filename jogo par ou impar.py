print('-=' * 10)
print('VAMOS JOGAR PAR OU IMPAR?')
print('-=' * 10)

from random import randint
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(1, 11)
    soma = jogador + pc
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = str(input('Par ou impar? [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {soma}.', end='')
    print('Deu Par' if soma % 2 == 0 else ' Deu impar')
    if par_impar == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif par_impar == 'I':
        if soma % 2 != 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {cont} vezes')