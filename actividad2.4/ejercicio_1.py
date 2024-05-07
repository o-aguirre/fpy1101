num = []
cont_impar = 0
cont_par = 0
list_impar = []
list_par = []

for i in num:
    if i % 2 == 1:
        cont_impar += 1
        list_impar.append(i)
    elif i % 2 == 0 and i != 0:
        cont_par += 1
        list_par.append(i)

if len(list_impar) == 0:
    list_impar = 0
    
if len(list_par) == 0:
    list_par = 0
    
print('Total números pares: ', cont_par, 'Números: ', list_par, sep='\n')
print('Total números impares: ', cont_impar, 'Números: ', list_impar, sep='\n')
