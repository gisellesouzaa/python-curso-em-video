dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
print('O total a pagar é de R$ {:.2f}'.format( 60 * dias + 0.15 * km))
