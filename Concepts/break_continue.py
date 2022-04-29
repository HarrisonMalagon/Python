def run():
    # for contador in range (1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print (i)
    #     if i ==5678:
    #         break
    # texto = input("Escribe un texto:")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    #Ciclo While con un  break
    dinero = int(input("Cuanto dinero tienes?: "))
    while dinero > 0:
        print("Dinero disponible: ", dinero)
        if dinero >= 3500:
            comprar=input("¿Desea comprar una cerveza? (s/n): ")
            if comprar == "s":
                print("Compra realizada")
                dinero = dinero - 3500
                print("Dinero restante: ", dinero)
                print("---Gracias por su compra---")

            elif comprar == "n":
                print("Compra cancelada")
                break
        else:
            print("No puedes comprar nada")
            break
def run2():
    while(True):
        print("oh oh, estas en un ciclo infinito")
        palabra = input("debes averiguar cual es la palabra correcta: ")
        oculta = "python"
        if palabra == oculta:
            break
    print("Felicidades has salido del ciclo infinito")    
        

if __name__ == "__main__":
    run2()

