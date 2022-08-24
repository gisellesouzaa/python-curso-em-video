extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez','onze', 'doze','treze','quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero de 0 a 20:'))
    if num >=0 and <=20:
        print(f'Você digitou o número {extenso[num]}.')
        break
    else: 
        print('Tente novamente.')
