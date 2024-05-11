total = 0
try:
    num = int(input('Ingrese un número: '))
    for i in range(1, (num + 1)):
        total += i
except:
    print('err')

print(total)