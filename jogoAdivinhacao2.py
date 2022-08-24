from random import randint
contador = 0
acertou = False
pc = randint(0,10)
print ('''Sou seu computador...
Pensei em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    contador += 1
    if jogador == pc:
        acertou = True
    else: 
        if jogador < pc:
            print('Mais... Tente mais uma vez!')
        elif jogador > pc:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(contador))
