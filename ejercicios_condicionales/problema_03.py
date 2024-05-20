# Solicita al usuario los coeficientes 𝑎a y 𝑏b de una expresión lineal 𝑎𝑥+𝑏ax+b y un valor 𝑥x. 
# Evalúa la expresión para ese 𝑥x y determina si el resultado es positivo, negativo o cero.

try:
    a_value = int(input('Ingresa valor de a: '))
    b_value = int(input('Ingresa valor de b: '))
    x_value = int(input('Ingresa valor de x: '))
except Exception as err:
    print(err.with_traceback)

total = (a_value * x_value) + (b_value*a_value*x_value) + b_value
print(total)