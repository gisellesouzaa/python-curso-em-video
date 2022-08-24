#gerer 5 num / colocar na tupla / exibir / ind maior e menor

from random import randint
tupla = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print('Os valores sorteados foram:', end='')
for n in tupla:
    print(n, end=' ')
print('\nO menor valor sorteado na tupla foi: {} \n O maior valor sorteado foi: {}'.format(max(tupla), min(tupla)))

