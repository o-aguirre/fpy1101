continents = {
    'europa': 1.5,
    'asia': .9,
    'oceania': 2.3
    }

try:
    name_receptor = input('Ingresa nombre receptor: ')
    phone = input('Ingresa número de contacto de receptor(9 dígitos): ')
    continent = input('Ingresa continente destino: \n1.-europa\n2.-asia\n3.-oceania\n: ')
    litros_export = int(input('Ingresa cantidad de litros a exportar: '))
except Exception as err:
    print(err.with_traceback)

eu_tamaño = .750
asia_tamaño = .700
oceania_tamaño = .850

tanktainer_lt = 12000
tanktainer_price = 3500

total_tanktainers = 0
if total_tanktainers % 12000 != 0:
    total_tanktainers = (total_tanktainers % 12000) + 1
else:
    total_tanktainers = total_tanktainers % 12000


#Validación nombre receptor
while len(name_receptor) < 2:
    name_receptor = input('Ingresa nombre receptor: ')

#Validación número teléfono
while len(phone) != 9:
    try:
        phone = (input('Ingresa número de contacto de receptor(9 dígitos): '))
    except Exception as err:
        print(err.with_traceback)

#Validación ubicación envios
while continent not in continents:
    continent = input('Ingresa continente destino: \n1.-europa\n2.-asia\n3.-oceania\n: ')

print(litros_export)

total_price = total_tanktainers * continents[continent]