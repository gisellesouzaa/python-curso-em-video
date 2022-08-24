# perguntar a distância da viagem
# calcule o valor da passagem sendo: R$ 0,50 por km rodado até 200km 
# e R$ 0,45 para viagens mais longas 

dist = float(input('Informe a distância da viagem em km: '))
print('Você está prestes a começar uma viagem de {:.1f} km.'.format(dist))
if dist<=200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O valor da sua passagem é {} R$ {:.2f}.'.format('\033[7;32;1m', preco))

# ALTERNATIVA:

# dist = float(input('Informe a distância da viagem em km: '))
# print('Você está prestes a começar uma viagem de {:.1f} km.'.format(dist))
# preco = dist * 0.50 if dist<=200 else dist * 0.45
# print('O valor da sua passagem é {} R$ {:.2f}.'.format('\033[7;32;1m', preco))
