#funcion palindromo
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#funcion del programa
def run():
    palabra = input("Ingrese una palabra: ")
    es_palindromo=palindromo(palabra)
    if es_palindromo == True:
        print("La palabra es palindromo")
    else:
        print("La palabra no es palindromo")


if __name__ =='__main__':
    run()