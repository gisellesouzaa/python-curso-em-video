#Legenda Cores
cor_fim = '\033[m'
cor_title = '\033[1;4;97;46m'
cor_inverter = '\033[1;7m'
cor_verde = '\033[1;42;97m'
cor_vermelha = '\033[1;41;97m'
cor_cinza = '\033[1;37;43m'

print('{}               JOKENPÔ             {}'.format(cor_title, cor_fim))
print('"-"' * 12)

jogador = int(input('''Para jogar contra o PC, escolha uma das opções abaixo:
  {0}1{1} PAPEL
  {0}2{1} PEDRA
  {0}3{1} TESOURA
  
Qual a sua jogada? '''.format(cor_inverter, cor_fim)))

from time import sleep
from random import choice
alternativas = [1, 2, 3]
pc = choice(alternativas)
ganhou = ('\n {}    Você ganhou!    {}'.format(cor_verde, cor_fim))
perdeu = ('\n {}    Você perdeu! Game over!     {}'.format(cor_vermelha, cor_fim))
empate = ('\n {}    Empatou!     {}'.format(cor_cinza, cor_fim))

print('\n O computador jogou... ', end='')
sleep(2)

if pc == 1:
    print('1 - papel')
elif pc == 2:
    print('2 - pedra')
else:
    print('3 - tesoura')



if jogador == 1 and pc == 2 or jogador == 2 and pc == 3 or jogador == 3 and pc == 1 :
    print(ganhou)
    
elif jogador == 1 and pc == 3 or jogador == 2 and pc == 1 or jogador == 3 and pc == 2:
    print(perdeu)
    
elif jogador ==  pc:
    print(empate)
