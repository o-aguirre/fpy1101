# Escribe un programa que solicite dos números y determine si son iguales, si el primero es mayor que el segundo o si el segundo es mayor que el primero

num_uno = int(input('Ingresa 1er número: '))
num_dos = int(input('Ingresa 2do número: '))

if num_uno == num_dos:
    print('Ambos números son iguales')
elif num_uno < num_dos:
    print('El 2do es mayor que el 1ro')
else:
    print('El 1ro es mayor que el 2do')