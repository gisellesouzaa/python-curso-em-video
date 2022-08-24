N = int(input('Informe 1 número inteiro para saber seu antecessor e seu sucessor:' ))
A = N-1
S = N+1
print('O antecessor de {} é {}, e seu sucessor é {}'.format (N, A, S))

# Outra alternativa:

N1 = int(input('Informe 1 número inteiro para saber seu antecessor e seu sucessor:' ))
print('Analisando o valor {}, o seu antecessor é {}, e seu sucessor é {}'.format (N1, (N1-1), (N1+1)))
