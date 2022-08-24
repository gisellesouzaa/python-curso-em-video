# ler 3 retas e informar se pode ou não formar um triângulo 

print ('-=-' * 30)
print ('ANALISADOR DE TRIANGULOS')
print ('-=-' * 30)
a = float(input('Insira o primeiro lado do triangulo: '))
b = float(input('Insira o segundo lado do triangulo: '))
c = float(input('Insira o terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a: 
    print('As medidas podem formar um triangulo')

    
else:
     print('As medidas informadas não formam um triangulo')

