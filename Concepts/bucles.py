#potencia de 2 con un while
def runw():
    limite=int(input("Establesca un limete para la potencia: "))
    i=0
    potencia2=2**i
    while potencia2 < limite:
        print("2 elevado a {} es igual a {}".format(i,potencia2))
        i+=1
        potencia2=2**i

#potencias de 2 con un for
def runf():
    limite=int(input("Establesca un limete para la potencia: "))
    for i in range(0,limite):
        print("2 elevado a {} es igual a {}".format(i,2**i))
    
    
if __name__== "__main__":
    runw()