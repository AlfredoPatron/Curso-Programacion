from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Hola {nombre}, he pensado un número entre el 1 y 100\nTienes 8 intentos para adivinarlo")

while intentos < 8:
    estimado = int(input("Cuál es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("El numero es mas alto")
    elif estimado > numero_secreto:
        print("El numero es mas bajo")
    else:
        print(f"Felidades {nombre}! Has adivinado el numero en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero era {numero_secreto}")