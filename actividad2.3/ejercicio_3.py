print("""Welcome to PEPE JHONS
      Escoge nuestras pizzas. Ingresa:
      1- Pizza vegetariana
      2- Pizza normal""")
ingredients_vegetarian = ['pimiento', 'cebolla', 'choclo', 'tofu']
ingredients_normal = ['pepperoni', 'jamon', 'chorizo', 'salmon']

pizza_choice = int(input())

if pizza_choice == 1:
    ingredients_choice_vegetarian1 = lower(input('Escoge un ingrediente. Pimiento, Cebolla, Choclo y tofu'))
    if ingredients_choice_vegetarian1 in ingredients_vegetarian:
        print('')
    ingredients_choice_vegetarian2 = input('Escoge un ingrediente. Pimiento, Cebolla, Choclo y tofu')
elif pizza_choice == 2:
    print('Debes escoger 2 ingredientes. Pepperoni, Jamón, Chorizo y Salmón')
    ingredients_choice_normal1 = input('Escoge un ingrediente. Pepperoni, Jamón, Chorizo y Salmón')
    ingredients_choice_normal2 = input('Escoge un ingrediente. Pepperoni, Jamón, Chorizo y Salmón')