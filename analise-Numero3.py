# Soma dos números ímpares que são múltiplos de 3. Intervalo de 1 a 500.

s = 0
for c in range(0, 501):
   if c % 2 != 0:
       if c % 3 == 0:
           s = s + c
print(s)
