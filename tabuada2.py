while True:
   print('--' * 10)
   n = int(input('Quer ver a tabuada de qual valor [numero negativo para parar]: '))
   if n <= 0:
       break
   for c in range(0, 10):
       print(f'{n} x {c:2} = {n*c}')
print('Programa finalizado. Volte sempre!')
