# Pide al usuario que ingrese una temperatura en grados Celsius.
#El programa debe clasificar la temperatura como 'Frío' si es menor a 10 grados, 'Templado'
#si está entre 10 y 25 grados, y 'Calor' si es mayor a 25 grados.

temp = int(input('Ingresa temperatura: '))

if temp < 10:
    print('Frio')
elif temp >= 10 and temp <= 25:
    print('Templado')
else:
    print('Calor')