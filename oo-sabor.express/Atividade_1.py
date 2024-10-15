class Restaurante:
    nome = ''
    categoria = 'Bistro'
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistro'
restaurante_praca.categoria = 'Italiana'
ativo = False

if restaurante_praca == ativo:
    print('Restaurante nao esta em funcionamento!')

else:
    print('Restaurante esta em funcionamento!')



restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('Se for pizzaria e fast food.')
else:
    print('Se nao for pizzaria, nao vai ser pizzaria!')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca.ativo)