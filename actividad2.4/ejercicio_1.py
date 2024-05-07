num = [1, 2, 3, 4, 5, 10, 23, 44]
cont_impar = 0
cont_par = 0
list_impar = []
list_par = []

for i in num:
    if i % 2 == 1:
        cont_impar += 1
        list_impar.append(i)
    else:
        cont_par += 1
        list_par.append(i)
        
print('Total números pares: ', cont_par, 'Números: ', list_par, sep='\n')
print('Total números impares: ', cont_impar, 'Números: ', list_impar, sep='\n')
