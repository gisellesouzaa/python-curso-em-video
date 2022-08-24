# Se puder formar triangulo descobrir se é: 
# equilátero todos os lados iguais
# isosceles: dois lados iguais
# escaleno todos diferentes

print ('-=-' * 30)
print ('ANALISADOR DE TRIANGULOS')
print ('-=-' * 30)
a = float(input('Insira o primeiro lado do triangulo: '))
b = float(input('Insira o segundo lado do triangulo: '))
c = float(input('Insira o terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a: 
    print('As medidas podem formar um triangulo')
    
    if a == b and b == c:
        print('O triangulo é equilátero: todos os lados são iguais.')
    
    elif a != b and b != c and c != a:
        print('O triangulo é escaleno: todos os lados são diferentes.')
    
    elif a == b or b == c or a == c:
        print('O triangulo é isosceles: e possui dois lados iguais.')
    
else:
     print('As medidas informadas não formam um triangulo')
