# def palindrome(string):
#     return string == string[::-1]
#Toda Funcion lambda puede convertirse a una funcion normal. No viceversa
palindrome= lambda string: string == string [::-1]

# print(palindrome('ana'))

def run ():
    palabra=input("Ingrese una palabra")
    if palindrome(palabra):
        print("Es un palindromo: ")
    else:
        print("No es un palindromo: ")


if __name__ == '__main__':
    run()