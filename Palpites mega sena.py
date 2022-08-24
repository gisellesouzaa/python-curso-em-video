# o programa pergunta quantos jogos será sorteado
# sorteia 6 numeros entre 1 e 50 para cada jogo 
# cadastrar tudo em uma lista composta
# não pode repetir numeros

from random import randint 
from time import sleep
print('-'*30)
print(f'JOGO DA MEGA SENA')
print('-'*30)
jogo=list()
sort=list()
quant = int(input(f'Quantos jogos você quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in sort:
            sort.append(num)
            cont += 1
        if cont >= 6:
            break
    sort.sort()
    jogo.append(sort[:])
    sort.clear()
    tot += 1
print(f'-=-=- SORTEANDO {quant} JOGOS -=-=-')
for i, l in enumerate(jogo):
    print(f'Jogo nº{i+1} é {l}')
    sleep(1)
print(f'-=-=- BOA SORTE! -=-=-')

