# Solicita al usuario tres números y determina cuál de ellos es el mayor, utilizando solamente condicionales
num_1 = int(input('Ingresa un número: '))
num_2 = int(input('Ingresa un número: '))
num_3 = int(input('Ingresa un número: '))

if num_1 > num_2 and num_1 > num_3:
    print('Número mayor es ', num_1)
elif num_2 > num_1 and num_2 > num_3:
    print('Número mayor es ', num_2)
else:
    print('Número mayor es ', num_3)
