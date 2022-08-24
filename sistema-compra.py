print('         LOJA SUPER BARATÃO          ')
print('-' * 40)
continua = 'S'
soma = 0
mais1000 = 0
menor_preco = 10000
menor_produto = ' '
while continua in 'Ss':
   produto = str(input('Nome do produto: '))
   preco = float(input('Preço: R$ '))
   soma += preco
   if preco >= 1000:
       mais1000 += 1
   if preco < menor_preco:
       menor_preco = preco
       menor_produto = produto
   continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'''O total da compra foi R${soma:.2f}
Temos {mais1000} custando mais de R$ 1.000,00
O produto mais barato foi {menor_produto} que custa R$ {menor_preco:.2f}''')
