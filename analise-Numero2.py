# ler 2 numeros inteiros e apresentar a analise:
# O primeiro valor e maior
# O segundo valor e maior
# Não existe valor maior, os dois são iguais

print ('-*-' * 15)
print ('Analisando o maior número:')
print ('-*-' * 15)

n1 = (float(input('Informe o primeiro número: ')))
n2 = (float(input('Informe o segundo número: ')))

if n1 > n2:
    print('Analisando os números digitados, verifiquei que o \033[1;31;43m primeiro \033[m valor é o maior.')
elif n2 > n1:
    print('Analisando os números digitados, verifiquei que o \033[1;31;43m segundo \033[m valor é o maior.')
elif n1 == n2:
    print('Analisando os números digitados, verifiquei que \033[1;31;43m não existe \033[m um número maior, os valores são iguais.')
        

