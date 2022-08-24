n = float(input('Informe a temperatura em °C: '))
print('A temperatura de {}°C corresponde a {}°F!'.format(n, ((n * 9/5) + 32)))

# neste caso como o cálculo segue a ordem de precedência, não necessita de parênteses 
# ex: print('A temperatura de {}°C corresponde a {}°F!'.format(n, (n * 9/5 + 32)))
