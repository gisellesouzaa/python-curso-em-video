import random
student1 = str(input('Primeiro aluno: '))
s2 = str(input('Segundo aluno: '))
s3 = str(input('Terceiro aluno: '))
s4 = str(input('Quarto aluno: '))
lista = [student1, s2, s3, s4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

#ALTERNATIVA:

# from random import choice
# student1 = str(input('Primeiro aluno: '))
# s2 = str(input('Segundo aluno: '))
# s3 = str(input('Terceiro aluno: '))
# s4 = str(input('Quarto aluno: '))
# lista = [student1, s2, s3, s4]
# escolhido = choice(lista)
# print('O aluno escolhido foi {}.'.format(escolhido))
