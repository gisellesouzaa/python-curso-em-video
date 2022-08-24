times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 
'Atlético-MG', 'Botafogo','Athletico-PR','Bahia', 
'São Paulo','Fluminense','Sport Recife', 'EC Vitória',
'Coritiba','Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 40)
print('Lista de times do Brasileirão 2017:')
for t in times:
    print(t)

print('-=' * 40)
print('Em que posição está o time da Chapecoense')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
