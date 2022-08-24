# Números pares de 1 a 50:

for c in range (0, 51):
   if c % 2 == 0:
       print(c)

# OU

for c in range (0, 51, 2):
   print (c, end=' - ')
print('Fim')
