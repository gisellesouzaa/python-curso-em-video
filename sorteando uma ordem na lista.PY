from random import shuffle
student1 = str(input('Primeiro aluno: '))
s2 = str(input('Segundo aluno: '))
s3 = str(input('Terceiro aluno: '))
s4 = str(input('Quarto aluno: '))

lista = [student1, s2, s3, s4]
shuffle(lista)
#shuffle = embaralhar

print ('A ordem de apresentação será: ')
print(lista)
