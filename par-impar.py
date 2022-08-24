# ler um numero inteiro
# falar se é par ou impar

num = int(input('\033[1;35m Insira um número qualquer: \033[m'))
rest_div = (num % 2) 
if rest_div == 0:
    print('O número {} é {}par{}.'.format(num, '\033[1;34m', '\033[m')) 
else: 
    print('O número {} é {}impar{}.'.format(num, '\033[1;34m', '\033[m'))
