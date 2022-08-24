# ler a velocidade de um carro
# se ultrapassar 80km por hora multado
# multa R$ 7 por cada km acima do limite

veloc = float(input('Informe a velocidade do carro: '))
if veloc> 80:
    print('\033[1;31m Você ultrapassou os 80km e recebeu uma multa de \033[1;33;41m R$ {:.2f}! \033[m'.format((veloc - 80)*7))
else: 
    print('\033[1;32m Bom dia. Dirija com segurança!')
