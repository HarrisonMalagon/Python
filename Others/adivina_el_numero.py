import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número entre 1 y 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido > numero_aleatorio:
            print("El número es más pequeño")
        else:
            print("El número es más grande")
        numero_elegido = int(input("Elige otro número: "))
    print("¡Felicidades! Elegiste el número correcto")

if __name__ == '__main__':
    run()