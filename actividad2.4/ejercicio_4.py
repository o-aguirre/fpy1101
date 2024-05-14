total = 0
precio = 0
descuento = 0

try:
    precio = int(input('Ingrese precio: '))
    descuento = int(input('Ingrese descuento: '))
    
except ValueError:
    print(ValueError)
except Exception as e:
    print('err', e.with_traceback)
finally:
    total = precio - (precio * (descuento / 100))
    print('Total: ', int(total))