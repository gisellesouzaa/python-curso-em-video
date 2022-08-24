palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado','programador', 'futuro')
for p in palavra:
    print('\n Na palavra {} temos: '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aáâãeéêiíou':
            print(letra.upper(), end=' ')
