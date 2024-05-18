continents = ['europa', 'asia', 'oceania']

try:
    name_receptor = input('Ingresa nombre receptor: ')
    phone = int(input('Ingresa número de contacto de receptor(9 dígitos): '))
    continent = input('Ingresa continente destino: \n1.-europa\n2.-asia\n3.-oceania\n: ')
    litros_export = int(input('Ingresa cantidad de litros a exportar: '))
except Exception as err:
    print(err)

eu_valor = 1.5
asia_valor = .9
oce_valor = 2.3

eu_tamaño = .750
asia_tamaño = .700
oceania_tamaño = .850

tanktainer_lt = 12000
tanktainer_price = 3500

if len(name_receptor) > 2:
    print(name_receptor)
if len(phone) == 9:
    print(phone)
if continent in continents:
    print(continent)
print(litros_export)


