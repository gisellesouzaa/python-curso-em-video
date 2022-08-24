from random import randint
from time import sleep #sistema “dorme” alguns segundos 
PC=randint (0, 5)
print('-==-' * 20)
print('Vou pensar em um numero entre 0 a 5. Tente adivinhar…')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
sleep(2)
if jogador == PC:
    print('Você acertou! Congratulations!!!')
else: 
    print('Você errou eu pensei no numero {} e não no {}! GAME OVER!'.format(PC, jogador))

