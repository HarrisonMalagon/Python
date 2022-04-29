# def saludo(func):
#     func()


# def hola():
#     print("Hola!!!")

# def adios():
#     print("Adios!!!")

# saludo(hola)
# saludo(adios)

# my_list = [1,2,3,4,5,7,8,9,13,19,21]
# odd = [i for i in my_list if i%2 !=0]
# print (odd)

#        FILTER
# La función filter recibe dos parámetros, en este caso:
# 1- una lambda que a su vez recibe un x devolviendo los x cuyo modulo de dos sean diferentes a 0
# 2- El segundo parámetro es el iterable my_list
# Al final todo se guarda dentro de la función list

my_list = [1,4,5,7,8,9,13,19,21]
odd= list(filter(lambda x : x%2 !=0, my_list))
print(odd)


#       MAP
# La función map recibe dos parámetros, en este caso:
# 1- una lambda que a su vez recibe un x devolviendo los x al cuadrado
# 2- El segundo parámetro es el iterable my_list2
# Al final todo se guarda dentro de la función list
my_list2 = [1,2,3,4,5]
squares = list(map(lambda x: x**2,my_list2))
print(squares)

#       REDUCE
# La función reduce recibe dos parámetros, en este caso:
# 1- Una lambda que a su vez recibe 2 parámetros a y b donde a es el valor del primer término y b el segundo
# 2- El segundo parámetro es el iterable my_list3
# Al final todo se reduce a un termino, a diferencia de filter y map, reduce debe ser importada del modulo functools

# my_list3=[2,2,2,2,2]
# all_multiplied = 1
# for i in my_list3:
#     print(all_multiplied,"--",i)
#     all_multiplied=all_multiplied*i
# print(all_multiplied)

from functools import reduce

my_list3=[2,2,2,2,2]

all_multiplied = reduce(lambda a,b: a*b, my_list3)

print(all_multiplied)