#Ejemplo de Tuplas vs Listas
lista=['Hola','Mundo',"!"]
tupla=('Hola','Mundo','!')
print(lista)
print(tupla)

numeros1=[1,2,3,4,5]
numeros2=[1,2,3,4,5]
Numeros1=(1,2,3,4,5)
Numeros2=(1,2,3,4,5,6,7,8)

listafinal=numeros1+numeros2
print(listafinal)
listafinal.append(6)

tuplafinal=Numeros1+Numeros2
print(tuplafinal)

print("\n")
print("Las Listas son Variables se ve la modificacion")
for numero in listafinal:
    print(numero)
print("Tuplas son inmutables")
for numero in tuplafinal:
    print(numero)