cant_user = int(input('Ingrese cantidad de personas que desean ingresar: '))
cont_user = 0
cont_child = 0
cont_teenager = 0
cont_adult = 0
total = 0

while cont_user < cant_user:
    cont_user += 1
    age = int(input('Ingrese su edad: '))

    if age > 0 and age < 4:
        print('La entrada es libre')
        cont_child += 1

    if age >= 4 and age <= 18:
        print('El valor de entrada es de $3500')
        cont_teenager += 1
        total += 3500

    if age > 18:
        print('El valor de entrada es de $5000')
        cont_adult += 1
        total += 5000

print(f"""Las cantifad de personas ingresadas fueron: 
      {cont_child} niños, {cont_teenager} adolecentes y {cont_adult} adultos.
      Valor total: {total}""")
