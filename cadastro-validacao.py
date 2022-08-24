sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Informação invalida.Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso!'.format(sexo))
