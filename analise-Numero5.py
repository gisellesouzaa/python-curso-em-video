from time import sleep
operador = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while operador != 5:
   print(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos numeros \n [5] sair do programa')
   operador = int(input('>>>>>>>>> Qual é a sua opção: '))
   if operador == 1:
       print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
       print('=-=' * 10)
       sleep(2)
   elif operador == 2:
       print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
       print('=-=' * 10)
       sleep(2)
   elif operador == 3:
       if n1 == n2:
           maior = 'ambos, pois os dois são iguais'
           print('=-=' * 10)
           sleep(2)
       elif n1 > n2:
           maior = n1
       else:
           maior = n2
       print(f'O maior valor entre {n1} e {n2} é {maior}')
       print('=-=' * 10)
       sleep(2)
   elif operador == 4:
       print('Informe os valores novamente: ')
       n1 = float(input('Primeiro valor: '))
       n2 = float(input('Segundo valor: '))
       print('=-=' * 10)
       sleep(2)
   else:
       print('Opção invalida. Tente novamente')
       print('=-=' * 10)
print('Obrigada! Volte sempre')