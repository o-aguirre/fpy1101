import random
random_num = random.randint(1, 10)
print(random_num)

while True:
    try:
        user_num = int(input('Ingrese un número: '))
    except:
        print('err')

    if user_num == random_num:
        print('HAZ ACERTADO!')
        break
    else:
        print('FALLASTE')
        if user_num < random_num:
            print('El número que buscas es mayor')
        else:
            print('El número que buscas es menor')

        