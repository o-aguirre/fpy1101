continents = {
    'europa': 1.5,
    'asia': .9,
    'oceania': 2.3
    }

try:
    #Validación nombre receptor
    name_receptor = input('Ingresa nombre receptor: ')
    while len(name_receptor) < 2:
        name_receptor = input('Ingresa nombre receptor: ')

    #Validación número teléfono
    phone = input('Ingresa número de contacto de receptor(9 dígitos): ')
    while len(phone) != 9:
        phone = (input('Ingresa número de contacto de receptor(9 dígitos): '))

    #Validación ubicación envios
    continent = input('Ingresa continente destino: \n1.-europa\n2.-asia\n3.-oceania\n: ').lower()
    while continent not in continents:
        continent = input('Ingresa continente destino: \n1.-europa\n2.-asia\n3.-oceania\n: ').lower()

    litros_export = int(input('Ingresa cantidad de litros a exportar: '))
except Exception as err:
    print(err.with_traceback)

#Calculo total containers
total_tanktainers = 0
if litros_export % 12000 != 0 :
    total_tanktainers = int(litros_export / 12000) + 1
else:
    total_tanktainers = litros_export / 12000

total_price_tanktainers = total_tanktainers * 3500

total_bottles = 0
total_price_bottles = 0

if continent == 'europa':
    total_bottles = int(litros_export / .750)
    total_price_bottles = total_bottles * continents[continent]
if continent == 'asia':
    total_bottles = int(litros_export / .7)
    total_price_bottles = total_bottles * continents[continent]
if continent == 'oceania':
    total_bottles = int(litros_export / .850)
    total_price_bottles = total_bottles * continents[continent]


print('Nombre receptor: ', name_receptor)
print('Teléfono: ', phone)
print('Continente destino: ', continent)
print('Cantidad de litros exportados: ', litros_export)
print('COTIZACION')
print('Tanktainers: ', total_tanktainers)
print('Valor Transporte: ', total_price_tanktainers)
print(f'Detalle botellas: {total_bottles} botellas x USD{continents[continent]} = {total_price_bottles}')
print('Costo total exportación: USD', total_price_bottles + total_price_tanktainers)