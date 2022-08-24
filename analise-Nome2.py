# pedir nome completo
# mostrar primeiro e último separado 

name = str(input('Digite o seu nome completo: ')).strip()
n = name.split()
print ('Primeiro: {}'.format(n[0]))
print ('Último: {}'.format(n[len(n)-1]))
#neste caso a função LEN identifica quantos itens existe na lista N.
