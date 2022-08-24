import math 
ang = float(input('Digite o ângulo que você deseja: '))
c = math.cos(math.radians(ang))
s = math.sin(math.radians(ang))
t = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, c))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, t))
