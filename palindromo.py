# leia uma frase e verifique se é um palindromo
# Ex. APOS A SOPA

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverter = ''
for letra in range(len(junto) - 1, -1, -1):
   inverter += junto[letra]
print(f'Você escreveu {junto} o inverso é {inverter}.')
if junto == inverter:
   print('A frase é um palíndromo.')
else:
   print('A frase não é um palímdromo.')
