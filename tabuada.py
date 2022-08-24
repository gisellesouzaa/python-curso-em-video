# Mostrar a tabuada de um número que o usuário escolher

n = int(input('insira um número para ver sua tabuada: '))
for c in range (0, 11):
   print ('{} x {:2} = {}'.format(n, c, n*c))
