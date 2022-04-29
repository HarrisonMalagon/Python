from multiprocessing import reduction


def palindrome(string):
    try:
        if len (string)==0:
            raise ValueError("No se puede ingresar una cadena de texto vacia")
        return string == string [::-1]
    except ValueError as ve:
        print(ve)
        return False
   
   
def run():
    palindrome("ana")


if __name__=='__main__':
    run()