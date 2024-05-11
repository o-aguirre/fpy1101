try:
    precio = int(input('Ingrese precio: '))
    descuento = int(input('Ingrese descuento: '))
except:
    print('err')

total = precio - (precio * (descuento / 100))

print('Total: ', int(total))