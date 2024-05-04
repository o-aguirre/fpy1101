user_earnings = int(input('Ingresa tu renta anual: '))

if user_earnings <= 550000:
    print('Tu impuesto será del 5%. Total de impuesto: ', user_earnings * .05)

if user_earnings > 550000 and user_earnings <=  860000:
    print('Tu impuesto será del 15%. Total de impuesto: ', user_earnings * .15)

if user_earnings > 860000 and user_earnings <= 935000:
    print('Tu impuesto será del 20%. Total de impuesto: ', user_earnings * .2)

if user_earnings > 935.000 and user_earnings <= 1305000:
    print('Tu impuesto será del 30%. Total de impuesto: ', user_earnings * .3)

if user_earnings > 1305000:
    print('Tu impuesto será del 45%. Total de impuesto: ', user_earnings * .4)