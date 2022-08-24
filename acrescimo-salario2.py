# ler o salario do funcionario e calcular o aumento
# salários > a R$ 1250 calcular aumento de 10%
# salários menores, calcular aumento de 15%

sal = float(input('Informe o valor do seu salário: '))
if sal >= 1250:
    print('Seu salário teve aumento de 10%. O salário atualizado é R$ {:.2f}.'.format(sal + (sal * 10/100)))
else:
    print('Seu salário teve aumento de 15%. O salário atualizado é R$ {:.2f}.'.format(sal+(sal*15/100)))
