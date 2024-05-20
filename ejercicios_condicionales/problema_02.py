# Pide al usuario las longitudes de los tres lados de un triángulo. El programadebe decir si el triángulo es equilátero, isósceles o escaleno
lado_uno = int(input('Ingresa el primer lado: '))
lado_dos = int(input('Ingresa el segundo lado: '))
lado_tres = int(input('Ingresa el tercer lado: '))

if lado_uno == lado_dos == lado_tres:
    print('Triángulo equilatero')
elif lado_uno == lado_dos and lado_uno != lado_tres:
    print('Triángulo isosceles')
elif lado_uno == lado_tres and lado_uno != lado_dos:
    print('Triángulo isosceles')
elif lado_tres == lado_dos and lado_uno != lado_tres:
    print('Triángulo isosceles')
else:
    print('Triangulo escaleno')
