import random, string

def generar_constrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    caracteres = MAYUS + MINUS + CHARS + NUMS
    contrasena = []

    for i in range(15):
        caracter_ramdom = random.choice(caracteres)
        contrasena.append(caracter_ramdom)
    print(contrasena)
    contrasena= ''.join(contrasena)
    return contrasena

def gerator_password():
    mayus=list(string.ascii_uppercase)
    minus=list(string.ascii_lowercase)
    chars=list(string.punctuation)
    nums=list(string.digits)
    caracter=mayus+minus+chars+nums
    password=[]

    for i in range(15):
        caracter_ramdom = random.choice(caracter)
        password.append(caracter_ramdom)
    print(password)
    password= ''.join(password)
    return password

def run():
    # contrasena = generar_constrasena()
    contrasena=gerator_password()
    print("Su contraseña es: " + contrasena)

if __name__ == '__main__':
    run()