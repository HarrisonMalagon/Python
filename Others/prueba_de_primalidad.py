def es_primo2(numero):
    contador=0
    for i in range(1,numero+1):
        if i==1 or i==numero:
            continue
        if numero%i==0:
            contador+=1
    if contador == 0:
        return True
    else:
        return False
def es_primo():
    numero = int(input("Escribe el número:  "))

    for i in range(2, numero):
        if numero % i == 0:
          print(numero%i)
          print("no es primo")
          break
        else:
            print(" si es primo")
            break

def run():
    es_primo()


if __name__ == "__main__":
    run()