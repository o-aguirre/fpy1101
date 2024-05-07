vocales = ['a', 'e', 'i', 'o', 'u']
cont_vocales = 0
cont_consonantes = 0

word = input('Ingresa una palabra: ').lower()

for i in word:
    if i in vocales:
        cont_vocales += 1
    else:
        cont_consonantes += 1

print('Número de vocales: ', cont_vocales)
print('Número de consonantes: ', cont_consonantes)