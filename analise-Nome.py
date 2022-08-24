# Pedir nome completo da pessoa
# mostrar o nome em maiúsculo
# mostrar o nome em minúsculo
# quantas letras tem ao todo sem espaço
# quantas letras tem o primeiro nome 

nome = str(input ('Insira seu nome completo: ')).strip()
#O ".strip" no final serve para tirar os espaços do inicio e final da frase.

print ('Seu nome em maiúsculo é {}'.format(nome.upper()))

print ('O nome em minúsculo é {}'.format(nome.lower()))

print ('Seu nome ao todo tem {} letras'. format(len(nome) - nome.count(' ')))

print ('Seu primeiro nome é {} e tem {} letras'. format(nome.split()[0], len(nome.split()[0])))



